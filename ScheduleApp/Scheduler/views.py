from django.shortcuts import render
import sqlite3
import os

################################################################################################################
#   
# Section: ViewSection  
# Holds all of the functions that will render differnt pages within the system.
#
################################################################################################################


#The starting point of the whole system
#Places the user on the login.html page
def login(request):
    return render(request, 'Login.html')


#Opens the UpdateProfile Webpage
def updateProfile(request):
    return render(request, 'UpdateProfile.html')


#Opens the UpdateProfile Webpage
def viewSchedule(request):
    return render(request, 'ViewSchedule.html')


#Opens the RequestTimeOff Webpage
def requestTimeOff(request):
    return render(request, 'RequestTimeOff.html')


#Opens the EnterAvailability Webpage
def enterAvailability(request):
    return render(request,'EnterAvailability.html')


#Opens the HomePage Webpage
def getHomePage(request):
    return render(request, 'StandardEmployeeHomepage.html')

##########################################################################################################
#
# Form Actions
#
##########################################################################################################

#This is the transition to the StandardEmployeeHomepage
#The user will reach this page after the login page if logged in successfully.
def loginAction(request):

    username = request.GET['username']
    password = request.GET['password']

    print("username: " + username)
    print("password: " + password)

    #checks connection in the database
    conn = sqlite3.connect('Schedule.db')
    print(checkConnection(conn))
    conn.close()


    return render(request, 'StandardEmployeeHomepage.html')


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


##########################################################################################################
#
# Helper Functions
#
##########################################################################################################

#This function checks if the database connection is opened or closed.
# will returns true for open and false for closed.
def checkConnection(conn):
    try:
        conn.cursor()
        return True 
    except Exception as ex:
        return False
