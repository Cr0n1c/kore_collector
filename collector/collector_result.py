
class CollectorResult(object):
    __slots__ = ["__events", "__entities", "__error_message"]

    def __init__(self, event_paths=None, entity_paths=None, error_message=None):
        self.__events = event_paths
        self.__entities = entity_paths
        self.__error_message = error_message

    def events(self):
        return self.__events if self.__events else []

    def entities(self):
        return self.__entities if self.__entities else []

    def is_error(self):
        return self.__error_message is not None

    def error_message(self):
        return str(self.__error_message)
