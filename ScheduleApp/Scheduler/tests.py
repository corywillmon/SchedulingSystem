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

class SaveDataTestCase(unittest.TestCase):
    def test_connect_to_schedule_database(self):
        dbservices = ScheduleDBServices()
        connected = False
        try:
            dbservices.openConnection()
            connected = True
        except Exception as ex:
            connected = False
        
        dbservices.close()

        self.assertTrue(connected)

    def test_connect_to_profile_database(self):
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
        dbservices.insertEmployee("John","1234")

        em = dbservices.findProfile("John","1234")
        dbservices.close()
        self.assertTrue(em.getflag())

    
    #Tested connecting to database and saving data in SaveDataTestCase

class RequestTimeOffTestCase(unittest.TestCase):
    def test_send_email(self):
        se = SendEmail()
        self.assertTrue(se.sendEmail("managerEmailTest@gmail.com", "test"))

    #Tested connecting to database and saving data in SaveDataTestCase

class UpdateScheduleTestCase(unittest.TestCase):
    sch = Schedule()
    sch.setID(2)
    sch.setDate("5-4-2021")
    sch.setDay("Monday")
    sch.setTime("12:00 PM")

    def test_edit_schedule_times(self):
        sch.setTime("1:00 PM")
        testword = sch.getTime()
        self.assertEqual("1:00 PM", testword)
    


class DeleteScheduleTestCase(unittest.TestCase):
    sch = Schedule()
    sch.setID(2)
    sch.setDate("5-4-2021")
    sch.setDay("Monday")
    sch.setTime("12:00 PM")
    sch.setUsername("testuser")

    def test_schedule_delete(self):
        dbservices = ScheduleDBServices()
        dbservices.openConnection()
        dbservices.createEmpSchedules()
        dbservices.insert(sch, "testuser")
        dbservices.delete("testuser", sch)

        newSch = dbservices.get("testuser")
        self.assertIsNull(newSch.getId())

    
    #Tested connecting to database and saving data in SaveDataTestCase

unittest.main()