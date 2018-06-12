# import requests
from .config import KoreClientConfig

class KoreClient(object):
    __slots__ = ["__config"]

    def __init__(self, kore_config):
        self.__config = KoreClientConfig(kore_config.client_config)

    def __str__(self):
        return "KoreClient: %s" % self.__config.get_url()

    def print_config(self):
        print(self.__config)
