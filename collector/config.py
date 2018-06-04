import yaml

class KoreConfig:
    __slots__ = ["client_config", "collector_config", "_plugin_configs", "plugin_names"]

    def __init__(self, config_path):
        conf = None
        with open(config_path) as config_file:
            conf = yaml.load(config_file)
        
        if conf.has_key("kore"):
            conf = conf["kore"]
        else:
            raise RuntimeError("Config file 'configuration.yaml' does not contain base key 'kore'")
        
        if conf.has_key("client"):
            self.client_config = conf["client"]
        else:
            raise RuntimeError("Config file 'configuration.yaml' is missing client config")

        if conf.has_key("collector"):
            self.collector_config = conf["collector"]
        else:
            raise RuntimeError("Config file 'configuration.yaml' is missing collector config")
        
        if conf.has_key("plugins"):
            self._plugin_configs = conf["plugins"]
            self.plugin_names = self._plugin_configs.keys()


    def get_plugin_config(self, plugin_name, plugin_config=None):
        if plugin_name not in self.plugin_names:
            raise RuntimeError("Config file 'configuration.yaml' is missing config for plugin: %s" % plugin_name)
        
        config = self._plugin_configs[plugin_name]
        if plugin_config:
            return plugin_config(config)
        
        return config
