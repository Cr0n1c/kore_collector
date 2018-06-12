""" LDAP source config
"""

class LdapConfig():
    __slots__ = ["bind_dn", "bind_passwd", "entity_names", "_ldap_filters"]

    def __init__(self, ldap_config):
        self.bind_dn = ldap_config["bind_dn"]
        self.bind_passwd = ldap_config["bind_passwd"]
        entities = ldap_config["entities"]
        self.entity_names = entities.keys()
        self._ldap_filters = entities

    def get_entity_filter(self, entity_name):
        return self._ldap_filters[entity_name]
