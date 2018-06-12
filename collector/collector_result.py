""" Collector Result

A collection of paths to files that should be uploaded to Kore Aggregator
"""
import os

class CollectorResult(object):
    __slots__ = ["__events", "__entities", "__error_message"]

    def __init__(self, event_paths=None, entity_paths=None, error_message=None):
        self.__events = event_paths
        self.__entities = entity_paths
        self.__error_message = error_message

    def __str__(self):
        result = "<CollectorResult:"
        if self.events():
            result += "\n Events:\n  * "
            result += "\n  * ".join(self.events())

        if self.entities():
            result += "\n Entities:\n  * "
            result += "\n  * ".join(self.entities())
        result += ">"
        return result

    def __add__(self, other):
        events = self.events() + other.events()
        entities = self.entities() + other.entities()
        message = None

        if self.error_message() and other.error_message():
            message = "* %s\n* %s" % (self.error_message().lstrip("* "),
                                      other.error_message().lstrip("* "))
        elif self.error_message():
            message = self.error_message()
        elif other.error_message():
            message = other.error_message()

        return CollectorResult(events, entities, message)

    def events(self):
        return self.__events if self.__events else []

    def entities(self):
        return self.__entities if self.__entities else []

    def is_error(self):
        return self.__error_message is not None

    def error_message(self):
        return str(self.__error_message) if self.__error_message else None

    def cleanup(self):
        files = self.events() + self.entities()
        for path in files:
            if os.path.isfile(path):
                os.remove(path)
