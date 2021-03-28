from django.urls import path
from . import views 

#this is how we will move from page to page.
#calling the functions that are in the views.py file.
urlpatterns = [
    path('', views.login, name='login'),
    path('loginAction', views.loginAction, name='loginAction'),
    path('updateProfile', views.updateProfile, name='updateProfile'),
    path('viewSchedule', views.viewSchedule, name='viewSchedule'),
    path('requestTimeOff', views.requestTimeOff, name='requestTimeOff'),
    path('enterAvailability', views.enterAvailability, name='enterAvailability'),
    path('backToHome', views.backToHome, name='backToHome')
]