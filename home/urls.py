from django import views
from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('',home,name='home'),
    path('download/<uid>/',download,name="download"),
]
