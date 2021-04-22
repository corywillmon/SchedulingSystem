import sqlite3
import os
from Backend.EmployeeProfile import EmployeeProfile

class ProfileDBServices:
    __conn = "" #__ makes the class member private

    def openConnection(self):
        self.__conn = sqlite3.connect('Profiles.db')
        self.__conn.execute('''CREATE TABLE IF NOT EXISTS profiles
                            (username       CHAR(100) UNIQUE NOT NULL,
                             password       CHAR(100) UNIQUE NOT NULL); ''')

    def close(self):
        self.__conn.close()

    def checkConnection(self):
        try:
            self.__conn.cursor()
            return True 
        except Exception as ex:
            return False


    #added a profile to the profiles table 
    def addProfile(self, username, password):
        sql = "INSERT INTO profiles (username, password) VALUES (?, ?);" #? are the arguments passed into the function
        arguments = (username, password)
        self.__conn.execute(sql, arguments) #this executes the sql command and the arguments tuple
        self.__conn.commit()


    #delects all profiles from the profiles table
    def selectAllProfiles(self):
        cursor = self.__conn.execute("SELECT * FROM profiles")
        for row in cursor:
            print('Username: ', row[0])
            print('Password: ', row[1])
        cursor.close()



    #finds a certain profile with the uname and password arguments
    def findProfile(self, uname, password):

        ep = EmployeeProfile()
        #need a profile object here to store the uname and password.
        sql ="SELECT username, password FROM profiles WHERE username = ? AND password = ?"
        arguments = (uname, password)
        cursor = self.__conn.execute(sql, arguments)

        found = False #flag to see if the user exist

        #Searches for user
        for row in cursor:
            if (uname == row[0] and password == row[1]):
                found = True
                ep.setFlag(found)
                ep.setUsername(row[0])
                ep.setPassword(row[1])

        cursor.close()

        #need to return the appropiate value here
        if found:
            print('Found')
            return ep
        else:
            ep.setFlag(found)
            return ep
            print('Not Found')