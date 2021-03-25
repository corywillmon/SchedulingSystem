from django.shortcuts import render

# Create your views here.

#The starting point of the whole system
#Places the user on the login.html page
def login(request):
    return render(request, 'Login.html')


#This is the transition to the StandardEmployeeHomepage
#The user will reach this page after the login page if logged in successfully.
def loginAction(request):
    return render(request, 'StandardEmployeeHomepage.html')