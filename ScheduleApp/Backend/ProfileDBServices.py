import sqlite3
import os

class ProfileDBServices:
    __conn = ""#sqlite3.connect('Profiles.db') #__ makes the class member private

    def openConnection(self):
        self.__conn = sqlite3.connect('Profiles.db')
        print('connection open')

    def close(self):
        self.__conn.close()
        print('connection closed')

    def checkConnection(self):
        try:
            self.__conn.cursor()
            return True 
        except Exception as ex:
            return False
