from django.contrib import admin
from django.urls import path
from myapp import views
from .models import info
urlpatterns = [
   path('' , views.upload , name='home')
]
