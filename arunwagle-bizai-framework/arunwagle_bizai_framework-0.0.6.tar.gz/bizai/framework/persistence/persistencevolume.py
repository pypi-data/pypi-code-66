
"""Use built-in abc to implement Abstract classes and methods"""

from abc import ABC, abstractmethod

class PersistentVolume(ABC):

    def __init__(self):
        print("PersistentVolume::init")
        self._instance = None

    """process method"""
    @abstractmethod
    def connect(self, **config):
        pass

class FilePersistenceVolume(PersistentVolume):
    
    """save method"""
    @abstractmethod
    def save(self):
        pass

    
    """save method"""
    @abstractmethod
    def get(self):
        pass

    """save method"""
    @abstractmethod
    def list(self):
        pass


    """save method"""
    @abstractmethod
    def delete(self):
        pass


class DBPersistenceVolume(PersistentVolume):
    
    @abstractmethod
    def set_autocommit_mode(self, mode):
        pass

    """save method"""
    @abstractmethod
    def insert(self):
        pass

    
    """save method"""
    @abstractmethod
    def update(self):
        pass

    """save method"""
    @abstractmethod
    def list(self):
        pass


    """save method"""
    @abstractmethod
    def upsert(self):
        pass

    