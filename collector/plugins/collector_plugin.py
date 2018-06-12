""" Collector plugin super class

This class handles saving data that has been collected to disk
"""

class CollectorPlugin(object):
    __slots__ = ["__tmp_dir"]

    def __init__(self, tmp_dir):
        self.__tmp_dir = tmp_dir

    def save(self, data):
        print(self.__tmp_dir)
        print(data)
