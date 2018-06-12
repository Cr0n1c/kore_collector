CONFIG_KEY_HOST = "aggregator_host"
CONFIG_KEY_PORT = "aggregator_port"
CONFIG_KEY_TOKEN = "aggregator_token"
CONFIG_KEY_USE_SSL = "aggregator_use_ssl"

class KoreClientConfig(object):
    __slots__ = ["__url", "__token"]

    def __init__(self, kore_client_config):
        config_keys = kore_client_config.keys()

        # TOKEN REQUIRED
        if CONFIG_KEY_TOKEN in config_keys:
            self.__token = kore_client_config[CONFIG_KEY_TOKEN]
        else:
            raise RuntimeError("Aggregator token not configured")

        # get url
        scheme = "http"
        if CONFIG_KEY_USE_SSL in config_keys:
            scheme = "https" if kore_client_config[CONFIG_KEY_USE_SSL] else "http"

        host = "localhost"
        if CONFIG_KEY_HOST in config_keys:
            host = kore_client_config[CONFIG_KEY_HOST]

        port = 18226
        if CONFIG_KEY_PORT in config_keys:
            port = int(kore_client_config[CONFIG_KEY_PORT])

        self.__url = "%s://%s:%d/" % (scheme, host, port)

    def __str__(self):
        return "<KoreClientConfig: %s>" % self.__url

    def get_url(self):
        return str(self.__url)

    def get_token(self):
        return str(self.__token)
