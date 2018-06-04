from collector.config import KoreConfig
from collector import plugins

CONFIG_YAML = "./var/conf/kore.yaml"

if __name__ == "__main__":
    print("[-] Loading config")
    kore_config = KoreConfig(CONFIG_YAML)
    args = ["ldap"]

    files = []
    for plugin_name in args:
        print("\t\t[-] Loading plugin: %s" % plugin_name)
        plugin = plugins.load_plugin(plugin_name)
        plugin_config = kore_config.get_plugin_config(plugin_name, plugin.config)

        collector = plugin.collector(plugin_config)
        collector.collect(kore_config.collector_config["tmp_dir"])
        

    print("[+] Starting up Collectors")
    # collector.client.KoreClient(kore_config)
