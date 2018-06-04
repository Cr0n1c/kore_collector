# Config for the LDAP collector

class LdapConfig():
    __slots__ = ["bind_dn", "bind_passwd", "entity_names", "_ldap_filters"]

    def __init__(self, ldap_config):
        self.bind_dn = ldap_config.get("bind_dn")
        self.bind_passwd = ldap_config.get("bind_passwd")
        entities = ldap_config.get("entities")
        self.entity_names = entities.keys()
        self._ldap_filters = entities

    def get_entity_filter(self, entity_name):
        return self._ldap_filters[entity_name]
