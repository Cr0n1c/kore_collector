""" Kore Collector module

This module is used to collect data from configured source and push it to the Kore Aggregator.
"""
import argparse
import os

from collector.client import KoreClient
from collector.config import KoreConfig
from collector import plugins, CollectorResult

DEFAULT_CONFIG_YAML = "./var/conf/kore.yaml"

def main():
    """ Main function
    """
    # parse args
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--config", dest="config_yaml", default=DEFAULT_CONFIG_YAML,
                        type=str, help="path to config file")
    parser.add_argument("--all", dest="all_sources", action='store_const', const=True,
                        default=False, help="dump all configured sources")
    parser.add_argument("--persist", dest="persist", action='store_const', const=True,
                        default=False, help="Persiste tmp data after completion")
    parser.add_argument(dest='source', nargs='*', default=[], type=str,
                        help='Sources to collects')
    args = parser.parse_args()

    # load config
    config_path = os.path.abspath(args.config_yaml)
    print("[-] Loading config from file: %s" % str(config_path))
    kore_config = KoreConfig(args.config_yaml)
    configured_plugins = kore_config.get_plugin_names()

    # verify source configs
    sources = []
    if args.all_sources:
        if "noop" in args.source:
            sources.append("noop")
        sources += configured_plugins
    else:
        for src in args.source:
            if src in configured_plugins:
                sources.append(src)
            elif str.lower(src) == "noop":
                sources.append("noop")
            else:
                print("\t[X] No config for source: %s" % src)
                exit(1)


    # load source plugins
    print("[+] Starting up Collectors")
    collectors = []
    for src in sources:
        print("\t[-] %s" % src)
        plugin = plugins.load_plugin(src)
        cfg_type = None
        if "config" in dir(plugin):
            cfg_type = plugin.config
        plugin_config = kore_config.get_plugin_config(src, cfg_type)
        collector = plugin.collector(kore_config.collector_config["tmp_dir"], plugin_config)
        collectors.append(collector)

    # collect
    collector_result = CollectorResult()
    print("[+] Collecting data")
    for collector in collectors:
        collector_result += collector.collect()

    print("[+] Uploading data...")
    client = KoreClient(kore_config)
    client.upload_results(collector_result)

    if not args.persist:
        print("[-] Cleaning up...")
        collector_result.cleanup()

if __name__ == "__main__":
    main()
