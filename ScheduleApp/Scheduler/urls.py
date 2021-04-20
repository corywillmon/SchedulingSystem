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
    path('getHomePage', views.getHomePage, name='getHomePage'),
    path('updateAction', views.updateAction, name='updateAction'),
    path('timeOffAction', views.timeOffAction, name='timeOffAction'),
    path('availabilityAction', views.availabilityAction, name='availabilityAction'),
    path('getManagerHomePage', views.getManagerHomePage, name='getManagerHomePage'),
    path('scheduleManager', views.scheduleManager, name='scheduleManager'),
    path('profileManager', views.profileManager, name='profileManager'),
    path('requestManager', views.viewRequests, name='requestManager'),
    path('logout', views.logout, name='logout')
]