from ..collector_plugin import CollectorPlugin
from config import LdapConfig

class Ldap(CollectorPlugin):
    __slots__ = ["_config"]

    def __init__(self, ldap_config):
        assert isinstance(ldap_config, LdapConfig)
        self._config = ldap_config
    
    def collect(self, tmp_dir):
        pass
