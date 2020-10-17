# -*- coding: utf-8 -*-

import os
import logging

from itest2.client import Client
from itest2.itest_session import ItestSession


CLIENT_TYPE = (ItestSession, )


class HttpClient(Client):
    """
    ItestSession管理类，包含ItestSession创建（创建后的对象添加到HttpClient）、ItestSession获取（可根据name获取）
    example:
        HttpClient.create_clients(conf.sessions)
        r = HttpClient.client('main').get('/test')
    """

    __instance = None
    clz = {}

    __default_headers = {}

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super(HttpClient, cls).__new__(
                cls, *args, **kwargs)
        return cls.__instance

    def client(self, name: str) -> ItestSession:
        """
        获取指定名称的ItestSession
        :param name: ItestSession对象name
        :return:
        """
        if name in self.__instance.__dict__.keys():
            return self.__instance.__getattribute__(name)
        else:
            logging.debug(f'http client {name} do not exist!')

    def create_clients(self, session_configs: tuple = None):
        """
        根据传入的配置创建ItestSession
        :param session_configs: (
            {
                "name": "default",
                "base_url": "https://www.default.com/base/",
                "headers": {"Content-Type": "application/json"}
            }
        ), header可以不配置，默认使用
        :return:
        """
        if session_configs is not None:
            for session_config in session_configs:
                if isinstance(session_config, dict):
                    self.create_client(
                        session_config.get("name") or "default",
                        session_config["base_url"],
                        session_config.get("headers") or self.__default_headers
                    )

        return self.__instance

    def create_client(self, name: str, base_url: str, headers: dict = {}):
        """
        创建 ItestSession
        :param name:
        :param base_url:
        :param headers:
        :return:
        """
        session = ItestSession()
        session.headers.update(headers)
        session.base_url = base_url
        self.__instance.__setattr__(name, session)
        logging.debug(
            f'create http client: name: {name}, uri: {base_url}, headers: {headers}')

        return self.__instance

    def close_all(self):
        for k, v in self.__instance.__dict__.items():
            if isinstance(v, CLIENT_TYPE):
                v.close()


# 初始化一个实例
_HTTP_CLIENTS = HttpClient()
