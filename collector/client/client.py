import requests

class KoreClient:
    __slots__ = ["config"]

    def __init__(self, kore_config):
        self.config = kore_config.client_config
