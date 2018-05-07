import importlib
import os

from glob import glob

CURRENT_SUB = __name__.split(".")[0]

# Import all files in this directory that end in .py and don't start with "_"
for f in glob(os.path.join(os.getcwd(), CURRENT_SUB, "*")):
    __all__ = []

    f_bname = os.path.basename(f)

    if not f_bname.startswith("_") and f_bname.endswith(".py"):
        mod_name = f_bname[:-3]
        importlib.import_module(".".join([CURRENT_SUB, mod_name]))
        __all__.append(mod_name)