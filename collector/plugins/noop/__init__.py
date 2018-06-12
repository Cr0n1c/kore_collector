""" A Noop collector plugin used for testing purposes
"""
from ..collector_plugin import CollectorPlugin
from ...collector_result import CollectorResult

class NoopPlugin(CollectorPlugin):
    """ This plugin collects nothing
    """
    def __init__(self, tmp_dir, noop_config):
        super().__init__(tmp_dir)

    def __str__(self):
        return "NoopCollectorPlugin"

    def collect(self):
        print("\t[-] %s" % str(self))
        return CollectorResult()

collector = NoopPlugin
