import sqlite3
import os
from Backend.EmployeeProfile import EmployeeProfile

class ProfileDBServices:
    __conn = "" #__ makes the class member private

    def openConnection(self):
        self.__conn = sqlite3.connect('Profiles.db')

    def close(self):
        self.__conn.close()

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



    #inserts employee record into the employees table
    def insertEmployee(self, id, name, position, username):
        self.createEmployeesTable(self.__conn)
        sql = "INSERT INTO employees (employeeID, name, position, username) VALUES (?, ?, ?, ?);"
        arguments = (id, name, position, username)
        self.__conn.execute(sql, arguments)
        self.__conn.commit()
        print('emp table created')


    #returns the employee object so that all of the data can be passed to the homepage 
    def findEmployeeInfo(self, username):
        ep = EmployeeProfile()
        sql = "SELECT * FROM employees WHERE username = ?"
        arguments = [username]
        cursor = self.__conn.execute(sql, arguments)

        for row in cursor:
            if username == row[3]:
                ep.setId(row[0])
                ep.setName(row[1])
                ep.setPosition(row[2])
                ep.setUsername(row[3])

        cursor.close()

        return ep



    def createProfilesTable(self, conn):
        self.__conn.execute('''CREATE TABLE IF NOT EXISTS profiles
                            (username       CHAR(100) UNIQUE NOT NULL,
                             password       CHAR(100) UNIQUE NOT NULL); ''')



    def createEmployeesTable(self, conn):
        self.__conn.execute('''CREATE TABLE IF NOT EXISTS employees
                                (employeeID     INT         PRIMARY KEY,
                                 name           CHAR(100)   NOT NULL,
                                 position       CHAR(100),
                                 username       CHAR(100)   UNIQUE NOT NULL,
                                 FOREIGN KEY (username) REFERENCES profiles(username)); ''')
