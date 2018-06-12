from .collector_result import CollectorResult
from .config import KoreConfig
# import plugins as p

# class Source:

#     def __init__(self, conf_file):
#         self.file = conf_file
#         self.yaml = self.parse_yaml()
#         self.server = None
#         self.user = None
#         self.cleartext_password = None
#         self.encrypted_password = None

#     def parse_yaml(self):
#         with open(self.file) as f:
#             return yaml.load(f.read())


# class ActiveDirectoryConf(Source):

#     def __init__(self, conf_file):
#         Source.__init__(self, conf_file)
#         self.activedirectory_dict = self.yaml.get("datasources").get("activedirectory")

#         if self.activedirectory_dict is None:
#             print("[!] Skipping Active Directory.  You did not supply [server, user, password]")
#             return

#         self.server = self.activedirectory_dict.get("server")
#         self.user = self.activedirectory_dict.get("user")
#         self.cleartext_password = self.activedirectory_dict.get("cleartext_password")


# class SccmConf(Source):

#     def __init__(self, conf_file):
#         Source.__init__(self, conf_file)
#         self.sccm_dict = self.yaml.get("datasources").get("sccm")

#         if self.sccm_dict is None:
#             print("[!] Skipping SCCM.  You did not supply [server, user, password]")
#             return

#         self.server = self.sccm_dict.get("server")
#         self.user = self.sccm_dict.get("user")
#         self.cleartext_password = self.sccm_dict.get("cleartext_password")


# class NessusConf(Source):

#     def __init__(self, conf_file):
#         Source.__init__(self, conf_file)
#         self.nessus_dict = self.yaml.get("datasources").get("nessus")

#         if self.nessus_dict is None:
#             print("[!] Skipping Nessus.  You did not supply [server, user, password]")
#             return

#         self.server = self.nessus_dict.get("server")
#         self.user = self.nessus_dict.get("user")
#         self.cleartext_password = self.nessus_dict.get("cleartext_password")


# class Configuration:

#     # __init__ will load all the modules that you will be working with
#     def __init__(self, conf_file):
#         self.neo4j = Neo4j(conf_file)  # This is the only required configuration

#         # data sources that we will attempt to parse
#         self.activedirectory = ActiveDirectoryConf(conf_file)
#         self.sccm = SccmConf(conf_file)
#         self.nessus = NessusConf(conf_file)
