""" A Noop plugin used for testing purposes
"""
from ..collector_plugin import CollectorPlugin
from ...collector_result import CollectorResult

class NoopPlugin(CollectorPlugin):
    def __init__(self, tmp_dir, ldap_config):
        pass

    def __str__(self):
        return "NoopCollectorPlugin"

    def collect(self):
        print("\t[-] %s" % str(self))
        return CollectorResult()

collector = NoopPlugin