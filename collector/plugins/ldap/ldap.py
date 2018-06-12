""" LDAP source plugin
"""
from ..collector_plugin import CollectorPlugin
from ...collector_result import CollectorResult
from .config import LdapConfig

class Ldap(CollectorPlugin):
    __slots__ = ["_config"]

    def __init__(self, tmp_dir, ldap_config):
        assert isinstance(ldap_config, LdapConfig)
        self._config = ldap_config
        super().__init__(tmp_dir)

    def __str__(self):
        return "LdapCollectorPlugin"

    def collect(self):
        print("\t[-] %s" % str(self))
        data = []
        data_file = super(Ldap, self).save(data)
        return CollectorResult(entity_paths=[data_file])
