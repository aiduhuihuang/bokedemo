from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path("index/",index),
    path("about/",about),
    path("gbook/",gbook),
    path("info/",info),
    path("list/",list),
    path("share/",share)
]