import os
import yaml

class KoreConfig:
    __slots__ = ["client_config", "collector_config", "__config_path", "__plugin_configs"]

    def __init__(self, config_path):
        conf = None
        with open(config_path) as config_file:
            conf = yaml.load(config_file)

        self.__config_path = os.path.abspath(config_path)

        if "kore" in conf.keys():
            conf = conf["kore"]
        else:
            raise RuntimeError("Config file 'configuration.yaml' does not contain base key 'kore'")

        if "client" in conf.keys():
            self.client_config = conf["client"]
        else:
            raise RuntimeError("Config file 'configuration.yaml' is missing client config")

        if "collector" in conf.keys():
            self.collector_config = conf["collector"]
        else:
            raise RuntimeError("Config file 'configuration.yaml' is missing collector config")

        if "plugins" in conf.keys():
            self.__plugin_configs = conf["plugins"]

    def get_config_path(self):
        return str(self.__config_path)

    def get_plugin_names(self):
        return list(self.__plugin_configs.keys())

    def get_plugin_config(self, plugin_name, plugin_config=None):
        config = self.__plugin_configs[plugin_name]
        if plugin_config:
            return plugin_config(config)

        return dict(config)
