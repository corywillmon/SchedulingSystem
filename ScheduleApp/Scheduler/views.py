from django.shortcuts import render
import sqlite3
import os

# Create your views here.

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
# End: ViewSection
#
##########################################################################################################


#This function checks if the database connection is opened or closed.
# will retur true for open and false for closed.
def checkConnection(conn):
    try:
        conn.cursor()
        return True 
    except Exception as ex:
        return False
