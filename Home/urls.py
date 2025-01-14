from django.urls import path, include 
from . import views

app_name = 'Home'

urlpatterns = [
    path('', views.Home, name='Home'),
    path('add/', views.addBirthday, name='addBirthday'),
]