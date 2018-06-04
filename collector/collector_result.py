
class CollectorResult:
    __slots__ = ["__events", "__entities", "error_message"]

    def __init__(self, event_paths = [], entity_paths = [], error_msg = None):
        self.__events = event_paths
        self.__entities = entity_paths
        self.error_message = error_msg
        pass

    def events(self):
        return self.__events

    def entities(self):
        return self.__entities

    def is_error(self):
        return self.error_message is not None
