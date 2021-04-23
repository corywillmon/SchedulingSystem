import os 
import sys
from Backend.Profile import Profile
from Backend.Schedule import Schedule

class EmployeeProfile(Profile):

    __employeeID = 0
    __name = ""
    __username=""
    __password=""
    __flag = False
    __position = ""
    __scheduleList = []
    
    def printInfo(self):
        print("Username: ", self.__username)
        print("Password: ", self.__password)
        print("Flag: ", self.__flag)

    def setId(self, id):
        self.__employeeID = id

    def setName(self, name):
        self.__name = name

    def setUsername(self, username):
        self.__username = username

    def setPassword(self, password):
        self.__password = password

    def setFlag(self, flag):
        self.__flag = flag
        
    def setPosition(self, position):
        self.__position = position

    def getId(self):
        return self.__employeeID

    def getName(self):
        return self.__name

    def getUsername(self):
        return self.__username

    def getPassword(self):
        return self.__password

    def getFlag(self):
        return self.__flag

    def getPosition(self):
        return self.__position

    def fillList(self, l):
        s = Schedule()
        for i in range(len(l)):
            s.setId(l[i].getId())
            s.setMonth(l[i].getMonth())
            s.setDay(l[i].getDay())
            s.setTime(l[i].getTime())
            s.setDate(l[i].getDate())
            self.__scheduleList.append(s)

    def printList(self):
        for i in range(len(self.__scheduleList)):
            print(self.__scheduleList[i].getId())
            print(self.__scheduleList[i].getMonth())
            print(self.__scheduleList[i].getDay())
            print(self.__scheduleList[i].getTime())
            print(self.__scheduleList[i].getDate())
