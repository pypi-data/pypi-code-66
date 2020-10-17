# -*- coding: utf-8 -*-

from itest2.client import Client
import records
import logging

CLIENT_TYPE = (records.Database, )


class DataBaseClient(Client):
    """
    数据库连接管理
    example:
        DBClient.create_clients(conf.databases)
        all = DBClient.client('moon').query('SELECT * FROM test_table LIMIT 10')
        DBClient.close()
    """

    __instance = None
    clz = {}

    __default_headers = {}

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super(DataBaseClient, cls).__new__(
                cls, *args, **kwargs)
        return cls.__instance

    def client(self, name: str) -> records.Database:
        """
        
        :param name: 
        :return:
        """
        if name in self.__instance.__dict__.keys():
            return self.__instance.__getattribute__(name)
        else:
            logging.debug(f'database client {name} do not exist!')

    def create_clients(self, conn_config: list = None):
        """
        根据传入的配置创建records.Database
        :param conn_config: (
            {
                "name": "pg",
                "uri": "postgresql://user:password@host:port/database"
            }
        )
        :return:
        """
        if conn_config is not None:
            for database in conn_config:
                if isinstance(database, ConfigTree):
                    self.create_client(database['name'], database['uri'])
        return self.__instance

    def create_client(self, name: str, uri: str):
        """
        指定名称和连接串创建records.Database
        :param name: records.Database对象名称
        :param uri: 数据库连接串
        :return:
        """
        if name in self.__instance.__dict__.values():
            if self.__instance.__getattribute__(name).open:
                return self.__instance
        self.__instance.__setattr__(name, records.Database(uri))
        logging.debug(f'create db client: name: {name}, uri: {uri}')
        return self.__instance

    def close_all(self):
        for k, v in self.__instance.__dict__.items():
            if isinstance(v, CLIENT_TYPE):
                v.close()


# 初始化一个实例
_DB_CLIENTS = DataBaseClient()