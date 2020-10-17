# -*- coding: utf-8 -*-

import abc


class Client(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def create_client(self):
        '''
        create client
        '''

    @abc.abstractmethod
    def client(self):
        '''
        get client
        '''

    @abc.abstractmethod
    def close_all(self):
        '''
        close client
        '''
