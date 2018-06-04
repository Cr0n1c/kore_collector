import importlib
import os

# from glob import glob0 as glob

# CURRENT_SUB = __name__.split(".")[0]
# __plugins = []

base = os.path.abspath(__name__)
# print base
# print glob(base, "*")
# # print glob())

# for plugin in glob(base, "*"):
#     print plugin
# os.path.abspath

# Import all files in this directory that end in .py and don't start with "_"
# for plugin in glob(os.path.join(, CURRENT_SUB, "*")):
#     plugin_name = os.path.basename(plugin)
#     print plugin_name
#     # if not plugin_name.startswith("_"):
    #     importlib.import_module(".".join([CURRENT_SUB, plugin_name]))
    #     __plugins.append(plugin_name)

def load_plugin(plugin_name):
    pkg = ".%s" % plugin_name
    return importlib.import_module(pkg, __name__)
