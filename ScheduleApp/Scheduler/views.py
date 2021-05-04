from django.shortcuts import render
import sqlite3
import os
import sys 

sys.path.append(".")
from Backend.ProfileDBServices import ProfileDBServices
from Backend.EmployeeProfile import EmployeeProfile
from Backend.Schedule import Schedule
from Backend.ScheduleDBServices import ScheduleDBServices

################################################################################################################
#   
# Navbar Transitions Between Pages
#
################################################################################################################

EMPLOYEE_DATA = EmployeeProfile()

#The starting point of the whole system
#Places the user on the login.html page
def login(request):
    return render(request, 'Login.html')


#Opens the UpdateProfile Webpage
def updateProfile(request):
    return render(request, 'UpdateProfile.html')


#Opens the ViewSchedule Webpage
def viewSchedule(request):

    #gets the schedule from the Schedules.db sends the records to the ViewSchedule page.
    db = ScheduleDBServices()
    db.open()
    l = db.get(EMPLOYEE_DATA.getUsername())
    EMPLOYEE_DATA.fillList(l)
    db.close()

    return render(request, 'ViewSchedule.html', {'list' : l})


#Opens the RequestTimeOff Webpage
def requestTimeOff(request):
    return render(request, 'RequestTimeOff.html')


#Opens the EnterAvailability Webpage
def enterAvailability(request):
    return render(request,'EnterAvailability.html')


#Opens the HomePage Webpage
def getHomePage(request):
    return render(request, 'StandardEmployeeHomepage.html', {'employee' : EMPLOYEE_DATA})


#Returns to the manager main homepage
def getManagerHomePage(request):
    return render(request, 'ManagerLogin.html')


#Opens the scheduleManager where all of the manager schedule related use cases will be
def scheduleManager(request):
    return render(request, 'ScheduleManager.html')


#Opens the profileManager where all of the manager profile related use cases will be
def profileManager(request):
    return render(request, 'ProfileManager.html')


#opens the manager side of the requestManager which will allow the manager to
#accept/deny time off request.
def viewRequests(request):
    return render(request, 'ViewRequests.html')


#returns to the main login page
def logout(request):
    return render(request, 'Login.html')





##########################################################################################################
#
# Form Actions
#
##########################################################################################################

#This is the transition to the StandardEmployeeHomepage
#The user will reach this page after the login page if logged in successfully.
def loginAction(request):

    ADMIN_USERNAME = "admin"
    ADMIN_PASSWORD = "salsa123"

    username = request.GET['username']
    password = request.GET['password']

    #The hardcoded login values to get into the manager side of the system.
    if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
        return render(request, 'ManagerLogin.html')

    #finds profile in the database
    db = ProfileDBServices()
    db.openConnection()
    ep = db.findProfile(username, password)
    db.close()

    #checks if employee is in the Profiles database
    if ep.getFlag():
        db.openConnection()
        employee = db.findEmployeeInfo(ep.getUsername())#sends employee data to the homepage for employees
        db.close()

        #global vaiable allows us to pass data between different pages when rendered.
        EMPLOYEE_DATA.setName(employee.getName())
        EMPLOYEE_DATA.setId(employee.getId())
        EMPLOYEE_DATA.setPosition(employee.getPosition())
        EMPLOYEE_DATA.setUsername(employee.getUsername())

        #print('EMPLYEE DATA: ', EMPLOYEE_DATA.getName())
        return render(request, 'StandardEmployeeHomepage.html', {'employee' : employee})
    else:
        return render(request, 'Login.html')


#This function updates the photo for the employee profile
#Once the action is completed, the user is notified of the success and returns to the main homepage.
def updateAction(request):
    photo = request.GET['file']

    #would save the photo here

    #print('photo was updated successfully')
    #return getHomePage(request)
    return render(request, 'UpdateProfile.html')


#This function handles the request on the RequestTimeOff page
#The date selected by the user is stored in a string
def timeOffAction(request):

    SUCCESS_MESSAGE = "Requested Time Off Was Sent Successfully"
    ERROR_MESSAGE = "Requested Time Off Was Not Sent Successfully"
    date = request.GET['selectDate']
    
    #TODO NEED TO PROCESS THE REQUEST HERE

    if date != "":
        return render(request, 'RequestTimeOff.html', {'message' : SUCCESS_MESSAGE})
    else:
        return render(request, 'RequestTimeOff.html', {'message' : ERROR_MESSAGE})


#This function handles the request from the EnterAvailability page.
#All of the data from the user is sent to this function. 
def availabilityAction(request):

    SUCCESS_MESSAGE = "Availability Was Sent Successfully"
    ERROR_MESSAGE = "Availability Was Not Sent Successfully"

    startDate = request.GET['startDate']
    endDate = request.GET['endDate']
    startTime = request.GET['startTime']
    endTime = request.GET['endTime']

    #TODO NEED TO PROCESS THE DATA HERE

    return render(request, 'EnterAvailability.html', {'message' : SUCCESS_MESSAGE})


#Function that handles the deletion of a schedule record from the Schedules db
def deleteScheduleAction(request):
    
    username = request.GET['username']
    date = request.GET['date']

    db = ScheduleDBServices()
    db.open()
    db.delete(username, date)
    db.close()

    return render(request, 'ScheduleManager.html')

#Function handles all updates to an employees scheudle from the manager side of the system.
def updateScheduleAction(request):

    username = request.GET['username']
    date = request.GET['date']
    time = request.GET['time']

    db = ScheduleDBServices()
    db.open()
    #update happens here
    db.close()


    return render(request, 'ScheduleManager.html')



#Function inserts a new schedule record into the system from the managers side.
def insertScheduleAction(request):
    
    schedule = Schedule()

    schedule.setUsername(request.GET['username'])
    schedule.setDay(request.GET['day'])
    schedule.setMonth(request.GET['month'])
    schedule.setTime(request.GET['time'])
    schedule.setDate(request.GET['date'])
    schedule.setId(request.GET['id'])

    db = ScheduleDBServices()
    db.open()
    db.insert(schedule, schedule.getUsername())
    db.close()

    return render(request, 'ScheduleManager.html')
