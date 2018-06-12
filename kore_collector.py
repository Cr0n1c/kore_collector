""" Kore Collector module

This module is used to collect data from configured source and push it to the Kore Aggregator.
"""
import argparse
import os

from collector.config import KoreConfig
from collector.client import KoreClient

DEFAULT_CONFIG_YAML = "./var/conf/kore.yaml"

def main():
    """ Main function
    """
    # parse args
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--config", dest="config_yaml", default=DEFAULT_CONFIG_YAML,
                        type=str, help="path to config file")
    parser.add_argument("-t", "--token", dest="config_yaml", default=None,
                        type=str, help="Kore Aggregator token")
    parser.add_argument("--all", dest="all_indicies", action='store_const', const=True,
                        default=False, help="dump all configured sources")
    parser.add_argument(dest='source', nargs='+', default=[], type=str,
                        help='Sources to collects')
    args = parser.parse_args()

    # load config
    config_path = os.path.abspath(args.config_yaml)
    print("[-] Loading config from file: %s" % str(config_path))
    kore_config = KoreConfig(args.config_yaml)
    configured_plugins = kore_config.get_plugin_names()

    # verify source configs
    sources = []
    for src in args.source:
        if src in configured_plugins:
            sources.append(src)
        else:
            print("\t[X] No config for source: %s" % src)
            exit(1)

    # load source plugins
    print("[+] Starting up Collectors")
    for src in sources:
        print("\t[-] Collecting from source: %s" % src)
        # plugin = plugins.load_plugin(plugin_name)
        # plugin_config = kore_config.get_plugin_config(plugin_name, plugin.config)

    print("[+] Uploading data...")
    client = KoreClient(kore_config)
    print(client)


if __name__ == "__main__":
    main()
