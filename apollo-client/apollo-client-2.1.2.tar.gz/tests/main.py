#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Date   : 2020/9/21
# @Author : Bruce Liu /Lin Luo
# @Mail   : 15869300264@163.com
from typing import Optional
from pyapollo.apollo_client import ApolloClient
from unittest import TestCase
from time import sleep


class TestClient(TestCase):
    def test_client(self):
        obj = ApolloClient(app_id='bruce_test', config_server_url='http://106.54.227.205:8090', cycle_time=30)
        self.assertEqual(obj.get_value('a'), 'gogogogo123456')
        self.assertEqual(obj.get_value('c', '123'), '123')
        print(obj.get_value('b'))
        # self.assertEqual(obj.get_value('b'), '123')
        sleep(120)
        print(obj.get_value('b'))
        # self.assertEqual(obj.get_value('b'), '234')
        self.assertEqual(obj.get_value('c1', '123', 'development.py-client'), '123')
