""" Collector plugin super class

This class handles saving data that has been collected to disk
"""
from abc import ABC, abstractmethod
import os
import uuid

from ..utils import file_utils

class CollectorPlugin(ABC):
    __slots__ = ["__tmp_dir"]

    def __init__(self, tmp_dir):
        self.__tmp_dir = os.path.abspath(tmp_dir)
        super().__init__()

    def save(self, data):
        dir_path = "%s/%s" % (self.__tmp_dir, str(self))
        os.makedirs(dir_path, exist_ok=True)
        path = "%s/%s.json.lz4" % (dir_path, uuid.uuid4())
        file_utils.dump(path, data)
        return path

    @abstractmethod
    def collect(self):
        pass
