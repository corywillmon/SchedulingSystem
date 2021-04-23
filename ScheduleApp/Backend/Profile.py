from abc import ABC, abstractmethod
class Profile(ABC):

    @abstractmethod
    def printInfo(self):
        pass

