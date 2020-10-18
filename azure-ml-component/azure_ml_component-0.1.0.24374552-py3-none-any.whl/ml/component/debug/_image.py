# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

import os
import sys
import json
import argparse
import psutil
import tempfile
from time import sleep
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor, Future
import subprocess
import threading
from pathlib import Path

from azure.ml.component._utils import pull_docker_image
from azureml._model_management._util import get_docker_client
from azureml.core.environment import Environment
from azureml.core import Workspace
from azure.ml.component._loggerfactory import _LoggerFactory, track

_logger = None

PULL_IMAGE_LOG = 'pull_image_log.txt'
BUILD_IMAGE_LOG = 'build_image_log.txt'


def _get_logger():
    global _logger
    if _logger is not None:
        return _logger
    _logger = _LoggerFactory.get_logger(__name__)
    return _logger


class ImageBase:
    def __init__(self, image_details, env, workspace, log_path=None):
        self.python_path = image_details['pythonEnvironment']['interpreterPath']
        self.env = env
        self.workspace = workspace
        self.image_details = image_details
        if not log_path:
            log_path = tempfile.gettempdir()
        # Image_name is stand for name of image in local.
        # And register_image_name is the name of image registered in ACR
        self.register_image_name = self.image_details['dockerImage']['name']
        self.log_path = os.path.join(log_path, self.register_image_name)

    @track(_get_logger)
    def get_module_image(self):
        _LoggerFactory.add_track_dimensions(_get_logger(),
                                            {'image_name': self.register_image_name})
        # Check image exists in docker
        checked_image_name = set([self.register_image_name])
        checked_image_name.add(self._get_image_name_from_image_details())
        self.image_name = self._check_image_existence(checked_image_name)
        if self.image_name:
            return self.image_name

        get_image_tasks = []
        # Pull image is a IO-bound task, using thread can improve performance.
        # pull image from remote
        thread_executor = ThreadPoolExecutor()
        stop_event = threading.Event()
        pull_image_future = thread_executor.submit(self.pull_image_remote, stop_event)
        get_image_tasks.append(pull_image_future)

        if not self.env.python.user_managed_dependencies:
            # Because Environment.build_local will create a subprocess to build image and not
            # support child pid to track it, we use process to execute it to track and terminate it.
            # build image processor
            env_str = json.dumps(Environment._serialize_to_dict(self.env))
            command = ['python', '-m', 'azure.ml.component.debug._image',
                       '--subscription_id', self.workspace._subscription_id,
                       "--resource_group", self.workspace._resource_group,
                       '--workspace_name', self.workspace._workspace_name,
                       '--env', env_str, '--log_path', self.log_path]
            build_process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE,
                                             stderr=subprocess.STDOUT, bufsize=1, universal_newlines=True)
            get_image_tasks.append(build_process)

        def wait_for_first_completion(tasks):
            """
            Wait for the first completion of getting image tasks.

            :param tasks: List of getting image tasks. And task supports subprocess and thread.
            :type tasks: list
            :return: First completion task
            :rtype: Future or Popen
            """
            time_run = 0
            sleep_period = 5
            timeout_seconds = sys.maxsize
            while len(tasks):
                if time_run + sleep_period > timeout_seconds:
                    raise ValueError('Timed out of waiting for getting module image.')
                for item in tasks:
                    if isinstance(item, Future):
                        try:
                            if not item.running():
                                item.result()
                                return item
                        except Exception:
                            # raise exception
                            print('Failed to pull image from remote registry.')
                            tasks.remove(item)
                    elif isinstance(item, subprocess.Popen):
                        returncode = item.poll()
                        if returncode == 0:
                            return item
                        elif returncode:
                            print('Failed to build image locally.')
                            tasks.remove(item)
                            pass
                time_run += sleep_period
                sleep(sleep_period)
            raise ValueError('Failed to get module image, diagnostic failure reason by logs\n'
                             f'\tlog path: {Path(self.log_path).resolve().absolute().as_posix()}.')

        completed_item = wait_for_first_completion([build_process, pull_image_future])
        docker_client = get_docker_client()
        # Delete temp images
        delete_image_list = []
        if completed_item == build_process:
            self.image_name = self.register_image_name
            pull_image_future.cancel()
            try:
                if pull_image_future.running():
                    stop_event.set()
                elif pull_image_future.done() and pull_image_future.result() != self.image_name:
                    delete_image_list.append(pull_image_future.result())
            except Exception:
                pass
        else:
            self.image_name = pull_image_future.result()
            for child in psutil.Process(build_process.pid).children(recursive=True):
                child.kill()
            build_process.terminate()
            if build_process.poll() == 0 and self.register_image_name != self.image_name:
                delete_image_list.append(self.register_image_name)
        delete_image_list.extend([item.id for item in docker_client.images.list(filters={'dangling': True})])

        # Building image locally will create a container. In order to avoid failure when terminate building process,
        # sleep one second to wait container closed.
        sleep(1)
        for item in delete_image_list:
            try:
                docker_client.images.remove(item, force=True)
            except Exception:
                print(f'Cannot delete image {item}')

        return self.image_name

    def _wait_for_image_build(self):
        detail = self.env.get_image_details(self.workspace)
        if not detail['imageExistsInRegistry']:
            build_info = self.env.build(self.workspace)
            print('Wait for remote image build completion.')
            build_info.wait_for_completion()
            detail = self.env.get_image_details(self.workspace)

            if not detail['imageExistsInRegistry']:
                raise Exception('Build image failed, image not in registry')
        return detail

    def _check_image_existence(self, image_names):
        docker_client = get_docker_client()
        exist_image_names = \
            list(filter(lambda image_name: len(docker_client.images.list(image_name)) > 0, image_names))
        if len(exist_image_names) > 0:
            return exist_image_names[0]
        else:
            return None

    def _get_image_name_from_image_details(self):
        registry = self.image_details['dockerImage']['registry']
        if not registry or not registry['address']:
            image_name = self.register_image_name
        else:
            image_name = '%s/%s' % (registry['address'], self.register_image_name)
        return image_name

    def pull_image_remote(self, stop_event=None):
        from azure.ml.component._module_run_helper import Logger
        with Logger(os.path.join(self.log_path, PULL_IMAGE_LOG), show_terminal=False):
            # Build image in acr
            detail = self._wait_for_image_build()
            # Pill image from acr
            docker_client = get_docker_client()
            registry = detail['dockerImage']['registry']
            if registry and registry['address']:
                image_name = '%s/%s' % (registry['address'], detail['dockerImage']['name'])
            else:
                image_name = detail['dockerImage']['name']
            start_time = datetime.now()
            pull_docker_image(
                docker_client, image_name, registry['username'], registry['password'], stop_event)
            print(f'Pull image from remote registry, cost {datetime.now() - start_time}')
        return image_name


class ModuleImage(ImageBase):
    def __init__(self, module, log_path=None):
        self.module = module
        image_detail, env = self._get_module_image_details()
        super(ModuleImage, self).__init__(
            image_detail, env, module.workspace, log_path)

    def _get_module_image_details(self):
        '''
        Getting environment of module by deserializing runconfig.
        Then registering module in workspace to get image detail.

        :return: image detail
        :rtype: dict
        '''
        # Get environment of module
        env_config = json.loads(self.module._module_dto.module_entity.runconfig)['Environment']

        # In Environment deserialize, keys need lowercase first letter
        def trans_config_key(config):
            new_config = {}
            for key in config.keys():
                lower_key = key[:1].lower() + key[1:]
                if isinstance(config[key], dict):
                    new_config[lower_key] = trans_config_key(config[key])
                else:
                    new_config[lower_key] = config[key]
            return new_config

        env_config = trans_config_key(env_config)
        env = Environment._deserialize_and_add_to_object(env_config)
        env.name = self.module.name
        env = env.register(self.module.workspace)
        detail = env.get_image_details(self.module.workspace)
        return detail, env


def build_image_local(subscription_id, resource_group, workspace_name, env_str, log_path):
    from azure.ml.component._module_run_helper import Logger
    with Logger(os.path.join(log_path, BUILD_IMAGE_LOG), show_terminal=False):
        env_dict = json.loads(env_str)
        env = Environment._deserialize_and_add_to_object(env_dict)
        workspace = Workspace._get_or_create(
            name=workspace_name,
            subscription_id=subscription_id,
            resource_group=resource_group)
        start_time = datetime.now()
        env.build_local(workspace, pushImageToWorkspaceAcr=False, useDocker=True)
        env.get_image_details(workspace)['dockerImage']['name']
        print(f'Built image locally, cost {datetime.now() - start_time}')


if __name__ == '__main__':
    # Using workspace and serialized environment info to build image locally
    parser = argparse.ArgumentParser(description='Execute image build locally for environment.')
    parser.add_argument('--subscription_id', type=str, help='Subscription id')
    parser.add_argument('--resource_group', type=str, help='Resource group')
    parser.add_argument('--workspace_name', type=str, help='Workspace name')
    parser.add_argument('--env', type=str, help='Serialized environment info')
    parser.add_argument('--log_path', type=str, help='Image build log path')

    args, _ = parser.parse_known_args(sys.argv)
    build_image_local(args.subscription_id, args.resource_group, args.workspace_name, args.env, args.log_path)
