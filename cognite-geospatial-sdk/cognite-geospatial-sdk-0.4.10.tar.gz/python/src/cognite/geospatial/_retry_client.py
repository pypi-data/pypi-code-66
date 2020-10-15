# Copyright 2020 Cognite AS
import logging
import os
import random
from functools import partial

from cognite.geospatial._client import ApiClient
from cognite.geospatial._client.exceptions import ApiException
from tornado.concurrent import Future
from tornado.ioloop import IOLoop

START_TIMEOUT = float(os.environ.get("TORNADO_RETRYCLIENT_START_TIMEOUT", "0.2"))
MAX_TIMEOUT = int(os.environ.get("TORNADO_RETRYCLIENT_MAX_TIMEOUT", "30"))
ATTEMPTS = int(os.environ.get("TORNADO_RETRYCLIENT_ATTEMPTS", "3"))
FACTOR = int(os.environ.get("TORNADO_RETRYCLIENT_FACTOR", "2"))

logger = logging.getLogger("RetryClient")


class RetryApiClient(ApiClient):
    def __init__(
        self,
        configuration=None,
        header_name=None,
        header_value=None,
        cookie=None,
        pool_threads=1,
        retry_attempts=ATTEMPTS,
        retry_start_timeout=START_TIMEOUT,
        retry_max_timeout=MAX_TIMEOUT,
        retry_factor=FACTOR,
        retry_for_statuses=None,
        retry_exceptions=None,
    ):
        super().__init__(
            configuration=configuration,
            header_name=header_name,
            header_value=header_value,
            cookie=cookie,
            pool_threads=pool_threads,
        )
        self.retry_attempts = retry_attempts
        self.retry_max_timeout = retry_max_timeout

        self.retry_start_timeout = retry_start_timeout
        if not retry_exceptions:
            self.retry_exceptions = ApiException
        else:
            self.retry_exceptions = retry_exceptions

        if not retry_for_statuses:
            self.retry_for_statuses = ()
        else:
            self.retry_for_statuses = retry_for_statuses
        self.retry_factor = retry_factor

    def request(
        self,
        method,
        url,
        query_params=None,
        headers=None,
        post_params=None,
        body=None,
        _preload_content=True,
        _request_timeout=None,
    ):
        attempt = 0
        future = Future()
        ioloop = IOLoop.current()
        raise_error = True
        request_call = super().request

        def handle_future(attempt, future_response):
            attempt += 1
            exception = future_response.exception()
            if exception:
                return handle_exception(attempt, exception)

            handle_response(attempt, future_response.result())

        def handle_response(attempt, result):
            response = result.tornado_response
            if response.error and attempt < self.retry_attempts and self._check_code(result.status):
                retry_wait = self._exponential_timeout(attempt)
                logger.warning(
                    "attempt: %d, %s request failed: %s, body: %s",
                    attempt,
                    response.effective_url,
                    response.error,
                    repr(result.data),
                )
                return ioloop.call_later(retry_wait, lambda: _do_request(attempt))

            if raise_error and response.error:
                return future.set_exception(response.error)

            future.set_result(result)

        def handle_exception(attempt, exception):
            retry_wait = self._exponential_timeout(attempt)
            logger.warning("attempt: %d, request failed with exception: %s", attempt, exception)
            if isinstance(exception, self.retry_exceptions) and attempt < self.retry_attempts:
                return ioloop.call_later(retry_wait, lambda: _do_request(attempt))

            return future.set_exception(exception)

        def _do_request(attempt):
            http_future = request_call(
                method,
                url,
                query_params=query_params,
                headers=headers,
                post_params=post_params,
                body=body,
                _preload_content=_preload_content,
                _request_timeout=_request_timeout,
            )
            http_future.add_done_callback(partial(handle_future, attempt))

        _do_request(attempt)

        return future

    def _exponential_timeout(self, attempt) -> float:
        # https://aws.amazon.com/blogs/architecture/exponential-backoff-and-jitter/
        timeout = self.retry_start_timeout * (self.retry_factor ** (attempt - 1))
        timeout = min(timeout, self.retry_max_timeout)
        return timeout / 2 + random.uniform(0, timeout / 2)

    def _check_code(self, code) -> bool:
        return code >= 500 and code <= 599 or code in self.retry_for_statuses
