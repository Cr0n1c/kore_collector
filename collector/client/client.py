# import requests
from .config import KoreClientConfig

class KoreClient(object):
    __slots__ = ["__config"]

    def __init__(self, kore_config):
        self.__config = KoreClientConfig(kore_config.client_config)

    def __str__(self):
        return "<KoreClient: %s>" % self.__config.get_url()

    def upload_results(self, collector_result):
        if collector_result.entities():
            print("\t[+] Entites")
            for file_path in collector_result.entities():
                print("\t\t[-] " + file_path)

        if collector_result.events():
            print("\t[+] Events")
            for file_path in collector_result.events():
                print("\t\t[-] " + file_path)
