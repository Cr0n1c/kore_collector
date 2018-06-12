import importlib

def load_plugin(plugin_name):
    pkg = ".%s" % plugin_name
    plugin = importlib.import_module(pkg, __name__)
    return plugin
    # return plugin(plugin_config)
