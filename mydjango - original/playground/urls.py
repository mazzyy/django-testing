from distutils.command.config import config
from django.urls import include
from django.urls import URLPattern, path 
from . import views



# ur config
URLPattern=[
    path('hello/',views.say_hello)
]