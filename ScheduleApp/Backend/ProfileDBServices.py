import sqlite3
import os

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
    #still needs a employee profile object
    #needs to return the object.
    def findProfile(self, uname, password):
        #need a profile object here to store the uname and password.
        cursor = self.__conn.execute("SELECT username, password FROM profiles WHERE username = ? AND password = ?",
                                     [uname, password])
        for row in cursor:
            uname = row[0]
            password = row[1]
        
        print(uname)
        print(password)
        cursor.close()
        #return the profile object