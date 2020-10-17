# -*- coding: utf-8 -*-

import requests
import logging

import curlify
import os
from itest2.json_schema import (validate_from_file, generate_to_file)
from itest2.response_assert import StatusCodeChecker
from hamcrest import assert_that, is_


class ItestSession(requests.Session):
    """
    继承requests.Session，
    1. 通过base_url定义基础url，其他请求通过path追加base_url为实际请求地址
    2. 覆写get post options head put patch delete，
        增加形参：sleep_time, timeout, status_code, schema_file 用来
        sleep_time: 服务请求失败后睡眠时间
        timeout: 可选，等待服务器响应的时常
        status_code: 响应状态码校验，如果为None不校验
        schema_file: 响应schema校验文件绝对路径，如果为None不校验
    3. headers参数逻辑修改
        不使用headers参数：默认使用MSession对象headers属性
        使用headers参数：
            d1 = {'a': 1, 'b': 2}
            d2 = {'b': 3, 'c': 4}
            {**d1, **d2} -> {'a': 1, 'b': 3, 'c': 4}
            {**self.headers, **kwargs['headers']}
    """

    def __init__(self):
        super(ItestSession, self).__init__()
        self.base_url = None

    def _request(self, method, path, sleep_time: int = 0, timeout: int = 5000,
                 status_code: int = None, schema_file: str = None, **kwargs):
        """

        :param method: 请求方法
        :param path: 请求子路径，base_url拼接path为实际请求路径
        :param sleep_time: 服务请求失败后睡眠时间，默认0s
        :param timeout: 可选，等待服务器响应的时常，默认5s
        :param status_code: 可选，响应状态码校验，如果为None不校验
        :param schema_file: 可选，响应schema校验文件绝对路径，如果为None不校验
        :param kwargs:
        :return:
        """
        # 请求地址
        url = f'{self.base_url}{"" if path.startswith("/") else "/"}{path}'
        # 更新headers
        if 'headers' in kwargs.keys():
            kwargs['headers'] = {**self.headers, **kwargs['headers']}
        r = None
        try:
            r = self.request(method, url, timeout=timeout, **kwargs)
            logging.info(f'''{curlify.to_curl(r.request)}''')
        except ConnectionError as e:
            sleep(sleep_time)
            raise ConnectionError()
        # 其他错误单独抛出
        if status_code:
            assert_that(r, is_(StatusCodeChecker(status_code)))
        if schema_file:
            if os.path.exists(schema_file):
                validate_from_file(r.json(), schema_file)
            else:
                generate_to_file(r.json(), schema_file)
        else:
            pass

        return r

    def get(self, path, params=None, sleep_time: int = 0, timeout: int = 5000,
            status_code: int = None, schema_file: str = None, **kwargs) -> requests.Response:
        """

        :param path: 请求子路径，base_url拼接path为实际请求路径
        :param params: (optional) Dictionary, list of tuples or bytes to send
        in the query string for the :class:`Request`.
        :param sleep_time: 服务请求失败后睡眠时间，默认0s
        :param timeout: 可选，等待服务器响应的时常，默认5s
        :param status_code: 可选，响应状态码校验，如果为None不校验
        :param schema_file: 可选，响应schema校验文件绝对路径，如果为None不校验
        :param kwargs:
        :return:
        """
        kwargs.setdefault('allow_redirects', True)
        return self._request('GET', path, params=params, sleep_time=sleep_time, timeout=timeout,
                             status_code=status_code, schema_file=schema_file, **kwargs)

    def post(self, path, data=None, json=None, sleep_time: int = 0, timeout: int = 5000,
             status_code: int = None, schema_file: str = None, **kwargs):
        """

        :param path: 请求子路径，base_url拼接path为实际请求路径
        :param data: (optional) Dictionary, list of tuples, bytes, or file-like
            object to send in the body of the :class:`Request`.
        :param json: (optional) json data to send in the body of the :class:`Request`.
        :param sleep_time: 服务请求失败后睡眠时间，默认0s
        :param timeout: 可选，等待服务器响应的时常，默认5s
        :param status_code: 可选，响应状态码校验，如果为None不校验
        :param schema_file: 可选，响应schema校验文件绝对路径，如果为None不校验
        :param kwargs:
        :return:
        """
        return self._request('POST', path,
                             data=data, json=json, sleep_time=sleep_time, timeout=timeout,
                             status_code=status_code, schema_file=schema_file, **kwargs)

    def options(self, path, sleep_time: int = 0, timeout: int = 5000,
                status_code: int = None, schema_file: str = None, **kwargs):
        """

        :param path: 请求子路径，base_url拼接path为实际请求路径
        :param sleep_time: 服务请求失败后睡眠时间，默认0s
        :param timeout: 可选，等待服务器响应的时常，默认5s
        :param status_code: 可选，响应状态码校验，如果为None不校验
        :param schema_file: 可选，响应schema校验文件绝对路径，如果为None不校验
        :param kwargs:
        :return:
        """
        kwargs.setdefault('allow_redirects', True)
        return self._request('OPTIONS', path, sleep_time=sleep_time, timeout=timeout,
                             status_code=status_code, schema_file=schema_file, **kwargs)

    def head(self, path, sleep_time: int = 0, timeout: int = 5000,
             status_code: int = None, schema_file: str = None, **kwargs):
        """

        :param path: 请求子路径，base_url拼接path为实际请求路径
        :param sleep_time: 服务请求失败后睡眠时间，默认0s
        :param timeout: 可选，等待服务器响应的时常，默认5s
        :param status_code: 可选，响应状态码校验，如果为None不校验
        :param schema_file: 可选，响应schema校验文件绝对路径，如果为None不校验
        :param kwargs:
        :return:
        """
        kwargs.setdefault('allow_redirects', False)
        return self._request('HEAD', path, sleep_time=sleep_time, timeout=timeout,
                             status_code=status_code, schema_file=schema_file, **kwargs)

    def put(self, path, data=None, sleep_time: int = 0, timeout: int = 5000,
            status_code: int = None, schema_file: str = None, **kwargs):
        """

        :param path: 请求子路径，base_url拼接path为实际请求路径
        :param data: (optional) Dictionary, list of tuples, bytes, or file-like
            object to send in the body of the :class:`Request`.
        :param sleep_time: 服务请求失败后睡眠时间，默认0s
        :param timeout: 可选，等待服务器响应的时常，默认5s
        :param status_code: 可选，响应状态码校验，如果为None不校验
        :param schema_file: 可选，响应schema校验文件绝对路径，如果为None不校验
        :param kwargs:
        :return:
        """
        return self._request('PUT', path, data=data, sleep_time=sleep_time, timeout=timeout,
                             status_code=status_code, schema_file=schema_file, **kwargs)

    def patch(self, path, data=None, sleep_time: int = 0, timeout: int = 5000,
              status_code: int = None, schema_file: str = None, **kwargs):
        """

        :param path: 请求子路径，base_url拼接path为实际请求路径
        :param data: (optional) Dictionary, list of tuples, bytes, or file-like
            object to send in the body of the :class:`Request`.
        :param sleep_time: 服务请求失败后睡眠时间，默认0s
        :param timeout: 可选，等待服务器响应的时常，默认5s
        :param status_code: 可选，响应状态码校验，如果为None不校验
        :param schema_file: 可选，响应schema校验文件绝对路径，如果为None不校验
        :param kwargs:
        :return:
        """
        return self._request('PATCH', path, data=data, sleep_time=sleep_time, timeout=timeout,
                             status_code=status_code, schema_file=schema_file, **kwargs)

    def delete(self, path, sleep_time: int = 0, timeout: int = 5000,
               status_code: int = None, schema_file: str = None, **kwargs):
        """

        :param path: 请求子路径，base_url拼接path为实际请求路径
        :param sleep_time: 服务请求失败后睡眠时间，默认0s
        :param timeout: 可选，等待服务器响应的时常，默认5s
        :param status_code: 可选，响应状态码校验，如果为None不校验
        :param schema_file: 可选，响应schema校验文件绝对路径，如果为None不校验
        :param kwargs:
        :return:
        """
        return self._request('DELETE', path, sleep_time=sleep_time, timeout=timeout,
                             status_code=status_code, schema_file=schema_file, **kwargs)
