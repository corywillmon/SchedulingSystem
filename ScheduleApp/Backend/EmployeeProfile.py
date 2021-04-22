import os 
import sys
from Backend.Profile import Profile

class EmployeeProfile(Profile):

    __username=""
    __password=""
    __flag = False
    
    def printInfo(self):
        print("Username: ", self.__username)
        print("Password: ", self.__password)
        print("Flag: ", self.__flag)

    def setUsername(self, username):
        self.__username = username

    def setPassword(self, password):
        self.__password = password

    def setFlag(self, flag):
        self.__flag = flag

    def getUsername(self):
        return self.__username

    def getPassword(self):
        return self.__password

    def getFlag(self):
        return self.__flag
