# Copyright 2020 Software Factory Labs, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import multiprocessing
from queue import Empty
from threading import Thread
from typing import Optional, Dict, List
from datetime import datetime
from collections import defaultdict
import random
import logging
from .job import Job
from . import events

random.seed()
logger = logging.getLogger(__name__)


class Executor:
    _lock: Optional[multiprocessing.RLock] = None

    def __init__(self, pool_size: int, scheduler):
        self._pool_size = pool_size  # TODO: use _pool_size
        self._scheduler = scheduler

        self._instances: Dict[int, Dict] = {}
        self._jobs_to_instances: Dict[str, List[int]] = defaultdict(list)
        self._recent_instance_ids: List[int] = []

        self.mp_ctx = multiprocessing.get_context('spawn')

        self._event_queue: Optional[multiprocessing.Queue] = None
        self._event_thread: Optional[Thread] = None
        self._running = False

    def setup(self):
        self._lock = self.mp_ctx.RLock()
        self._event_queue = self.mp_ctx.Queue()

        self._event_thread = Thread(target=self._event_read_loop, daemon=True)
        self._running = True
        self._event_thread.start()

    def teardown(self, wait: bool = True):
        logger.debug('Tearing down...')

        processes = [instance['process'] for instance in self._instances.values()]
        logger.debug(f'Processes: {processes}')

        while alive_processes := [process for process in processes if process.is_alive()]:
            logger.debug(f'Alive processes: {alive_processes}')
            for process in alive_processes:
                logger.debug(f'Process: {process}')
                if not wait:
                    logger.debug('    terminating')
                    process.terminate()
                logger.debug('    joining')
                process.join(1)
                if not process.is_alive():
                    logger.debug('    closing')
                    try:
                        process.close()
                    except ValueError:
                        pass
                else:
                    logger.debug('    still alive; will try again soon')

        self._instances = {}
        self._jobs_to_instances = {}

        self._lock = None

        logger.debug('Closing event thread')
        self._running = False
        self._event_thread.join()
        logger.debug('Deleting event thread')
        del self._event_thread
        logger.debug('Closing event queue')
        self._event_queue.close()
        self._event_queue.join_thread()

        logger.debug('Done')

    def submit_job(self, job: Job, run_time: datetime) -> int:
        if self._lock is None:
            raise ExecutorNotSetupException

        with self._lock:
            if job.max_instances != -1 and len(self._jobs_to_instances[job.id]) >= job.max_instances:
                raise MaxJobInstancesReachedException(job, self._jobs_to_instances[job.id])

            dynamic_args = {}
            for arg_name, values in job.dynamic_args.items():
                func = values['func']
                dynamic_args[arg_name] = func()

            instance_id = self._gen_new_instance_id()
            process = self.mp_ctx.Process(target=run_job, name=f'Process-{instance_id}',
                                          args=(job, instance_id, run_time, self._event_queue),
                                          kwargs=dynamic_args)

            self._instances[instance_id] = {
                'job': job,
                'id': instance_id,
                'start_time': datetime.now(tz=self._scheduler.tz),
                'process': process
            }

            self._jobs_to_instances[job.id].append(instance_id)

            try:
                logger.info(f'Running job "{job.id}" (scheduled at {run_time})')
                process.start()
            except Exception:
                self._job_cleanup(job.id, instance_id, terminate=True)
                raise

            return instance_id

    def terminate_job(self, instance_id: int):
        with self._lock:
            instance = self._instances.get(instance_id, None)

            if instance is None:
                raise JobInstanceNotFoundException(instance_id)

        self._job_cleanup(instance['job'].id, instance_id, terminate=True)

    def get_job_instance_ids(self, job_id: str) -> List[int]:
        with self._lock:
            return self._jobs_to_instances.get(job_id, [])

    def get_job(self, instance_id: int) -> Job:
        with self._lock:
            instance = self._instances.get(instance_id, None)
            if instance is None:
                raise JobInstanceNotFoundException(instance_id)

            return instance['job']

    def get_instances(self) -> List[dict]:
        with self._lock:
            return list(self._instances.values())

    def _event_read_loop(self):
        logger.debug('waiting for event...')
        while self._running:
            try:
                event: events.JobExecutionEvent = self._event_queue.get(timeout=0.2)
            except Empty:
                continue

            logger.debug(f'got event ({event}) from job {event.job_id}:{event.instance_id}; '
                         f'event queue size: {self._event_queue.qsize()}')

            if event.success:
                logger.info(f'Job "{event.job_id}" executed successfully')
            else:
                logger.error(f'Job "{event.job_id}" raised an exception\n{event.formatted_exc}')

            self._job_cleanup(event.job_id, event.instance_id)
            self._scheduler._dispatch_event(event)

            logger.debug('waiting for event...')

    def _job_cleanup(self, job_id: str, instance_id: int, terminate: bool = False):
        with self._lock:
            process = self._instances[instance_id]['process']

            logger.debug(f'cleaning up instance (job_id: {job_id}, instance_id: {instance_id}, process: {process})')

            if process.is_alive():
                if terminate:
                    logger.debug(f'terminating process')
                    try:
                        process.terminate()
                    except Exception as e:
                        logger.exception(e)
                process.join(timeout=2)

            if not process.is_alive():
                process.close()
                logger.debug('process closed')
            else:
                logger.error('Could not terminate process')

            logger.debug(f'instances: {self._instances}')
            logger.debug(f'mapping: {dict(self._jobs_to_instances)}')

            logger.debug('removing instance')
            del self._instances[instance_id]
            self._jobs_to_instances[job_id].remove(instance_id)

            logger.debug(f'instances: {self._instances}')
            logger.debug(f'mapping: {dict(self._jobs_to_instances)}')

            logger.debug('cleaned up')

    def _gen_new_instance_id(self) -> int:
        with self._lock:
            while (instance_id := random.randint(1000, 9999)) in list(self._instances.keys()) + self._recent_instance_ids:
                pass

            self._recent_instance_ids.append(instance_id)
            if len(self._recent_instance_ids) > 1000:
                self._recent_instance_ids.pop(0)

            return instance_id


def run_job(job: Job, instance_id: int, run_time: datetime, event_queue: multiprocessing.Queue, **kwargs):
    try:
        retval = job.func(job.id, instance_id, *job.args, **job.kwargs, **kwargs)
        logger.debug(f'job {job.id}:{instance_id} returned {retval}')
    except Exception as e:
        logger.debug(f'job {job.id}:{instance_id} raised an exception')
        event = events.JobExecutionEvent(events.EVENT_JOB_EXECUTED, job.id, instance_id, run_time, success=False,
                                         exc=e)
    else:
        logger.debug(f'job {job.id}:{instance_id} executed successfully')
        event = events.JobExecutionEvent(events.EVENT_JOB_EXECUTED, job.id, instance_id, run_time, success=True,
                                         retval=retval)

    logger.debug(f'sending event to queue ({job.id}:{instance_id})')
    [h.flush() for h in logger.handlers]
    event_queue.put(event)
    logger.debug(f'event queue size: {event_queue.qsize()} ({job.id}:{instance_id})')


class ExecutorNotSetupException(Exception):
    pass


class MaxJobInstancesReachedException(Exception):
    def __init__(self, job: Job, instance_ids: List[int]):
        super().__init__(f'Job "{job.id}" has already reached its maximum number of instances '
                         f'({job.max_instances})')
        self.job = job
        self.instance_ids = instance_ids


class JobInstanceNotFoundException(Exception):
    def __init__(self, instance_id: int):
        super().__init__(f'Job instance {instance_id} not found')
        self.instance_id = instance_id
