from ..config import KoreConfig

class CollectorPlugin:
    __slots__ = ["__config"]

    def __init__(self):
        pass

    def save(self, tmp_dir, entities):
        print tmp_dir
