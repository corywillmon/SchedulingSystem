from abc import ABC, abstractmethod
class Profile(ABC):
        
    @abstractmethod
    def printprofile(self):
        pass

class ManagerProfile(Profile):
    def printprofile(self):
        print("I am a manager")
        
class EmployeeProfile(Profile):
    def printprofile(self):
        print("I am an employee")
        
P = ManagerProfile()
P.printprofile()

E = EmployeeProfile()
E.printprofile()
