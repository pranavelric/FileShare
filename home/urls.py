from django import views
from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', HandleFileUpload.as_view(),name="handle_file_view"),
]
