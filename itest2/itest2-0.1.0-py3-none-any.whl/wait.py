# -*- coding: utf-8 -*-
import time

from itest.exceptions import TimeoutException

POLL_FREQUENCY = 0.5  # How long to sleep inbetween calls to the method
# exceptions ignored during calls to the method
IGNORED_EXCEPTIONS = (TimeoutException,)


class IWait(object):
    """
    传入对象和超时时间，默认每0.5s调用一次lambda表达式，判断成立/不成立
    """

    _ignored_exceptions = ...

    def __init__(self, obj, timeout,
                 poll_frequency=POLL_FREQUENCY, ignored_exceptions: list = None):
        """
        显性等待，指定等待时间判断方法执行输出成立、输出不成立
        Example:
            from TestUtils.http_client import HttpClient

            IWait(HttpClient, 8).until(lambda x: x.client('main').get('/test').status_code == 200)
            IWait(DBClient, 10).until_not(
            lambda x: x.client('growing').query(
                'select state from table where id = 10')[0][0] == 'activated'
        )
        :param obj:
        :param timeout: Number of seconds before timing out
        :param poll_frequency: sleep interval between calls By default, it is 0.5 second.
        :param ignored_exceptions: iterable structure of exception classes ignored during calls.
            By default, it contains TimeoutException only.
        """
        self._obj = obj
        self._timeout = timeout
        self._poll = poll_frequency
        # avoid the divide by zero
        if self._poll == 0:
            self._poll = POLL_FREQUENCY
        exceptions = list(IGNORED_EXCEPTIONS)
        if ignored_exceptions is not None:
            try:
                exceptions.extend(iter(ignored_exceptions))
            except TypeError:  # ignored_exceptions is not iterable
                exceptions.append(ignored_exceptions)
        self._ignored_exceptions = tuple(exceptions)

    def __repr__(self):
        return '<{0.__module__}.{0.__name__} (session="{1}")>'.format(
            type(self), self._obj.session_id)

    def until(self, method, message=''):
        """Calls the method provided with the obj as an argument until the \
        return value is not False."""
        screen = None
        stacktrace = None

        end_time = time.time() + self._timeout
        while True:
            try:
                value = method(self._obj)
                if value:
                    return value
            except self._ignored_exceptions as exc:
                screen = getattr(exc, 'screen', None)
                stacktrace = getattr(exc, 'stacktrace', None)
            time.sleep(self._poll)
            if time.time() > end_time:
                break
        raise TimeoutException(
            f'''Timeout Error: message: {message}, screen: {screen}, stacktrace: {stacktrace}''')

    def until_not(self, method, message=''):
        """Calls the method provided with the obj as an argument until the \
        return value is False."""
        end_time = time.time() + self._timeout
        while True:
            try:
                value = method(self._obj)
                if not value:
                    return value
            except self._ignored_exceptions as exc:
                return True
            time.sleep(self._poll)
            if time.time() > end_time:
                break
        raise TimeoutException(f'''Timeout Error: message: {message}''')
