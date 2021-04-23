from abc import ABC, abstractmethod

class SendServices(ABC):
    @abstractmethod
    def sendEmail(self, recipient):
        pass