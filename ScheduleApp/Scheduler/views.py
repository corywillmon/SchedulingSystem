from django.shortcuts import render
import sqlite3
import os

# Create your views here.

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


def updateProfile(request):
    return render(request, 'UpdateProfile.html')


#This function checks if the database connection is opened or closed.
# will retur true for open and false for closed.
def checkConnection(conn):
    try:
        conn.cursor()
        return True 
    except Exception as ex:
        return False
