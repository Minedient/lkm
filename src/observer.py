from abc import ABC, abstractmethod
class Announcer:
    """
    A class that manages observers and notifies them of events.
    A key element of the Observer pattern.
    """
    def __init__(self):
        self._observers : list[Observer] = []

    def notify(self, event_type, *args, **kwargs):
        for observer in self._observers:
            observer.notifyUpdate(event_type, *args, **kwargs)
    
    def register(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def unregister(self, observer):
        if observer in self._observers:
            self._observers.remove(observer)


class Observer(ABC):
    """
    A base class for observers. Observers should inherit from this class and implement the update method.
    A key element of the Observer pattern.
    """
    @abstractmethod
    def notifyUpdate(self, event_type, *args, **kwargs):
        """
        To be implemented by subclasses.
        This method will be called when an event is triggered.
        """
        pass