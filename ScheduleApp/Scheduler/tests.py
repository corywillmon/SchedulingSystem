import unittest
from django.shortcuts import render
import sqlite3
import os
import sys 

#I honestly have no idea how to make this work any other way, just copy your filepath to ScheduleApp below to run the tests
sys.path.insert(1, 'C:/Users/Tyler/Desktop/Programming Files/IT326/SchedulingSystem/ScheduleApp')
from Backend.ProfileDBServices import ProfileDBServices
from Backend.EmployeeProfile import EmployeeProfile
from Backend.Schedule import Schedule
from Backend.ScheduleDBServices import ScheduleDBServices
from Backend.SendEmail import SendEmail

# Create your tests here.
class CreateProfileTestCase(unittest.TestCase):
    def test_manager_create(self):
        pass

    def test_create_employee(self):
        em = EmployeeProfile()
        self.assertIsNotNone(em)

    def test_connect_to_database(self):
        dbservices = ProfileDBServices()
        connected = False
        try:
            dbservices.openConnection()
            connected = True
        except Exception as ex:
            connected = False
        
        dbservices.close()

        self.assertTrue(connected)

    def test_profile_create(self):
        dbservices = ProfileDBServices()
        dbservices.openConnection()
        dbservices.createProfilesTable("")
        dbservices.addProfile("John","1234")

        em = dbservices.findProfile("John","1234")
        dbservices.close()
        self.assertTrue(em.getflag())

class RequestTimeOffTestCase(unittest.TestCase):
    def test_send_email(self):
        se = SendEmail()
        self.assertTrue(se.sendEmail("tylerfreed2001@gmail.com", "test"))

    def test_connect_to_database(self):
        dbservices = ProfileDBServices()
        connected = False
        try:
            dbservices.openConnection
            connected = True
        except Exception as ex:
            connected = False
        
        dbservices.close()

        self.assertTrue(connected)

unittest.main()