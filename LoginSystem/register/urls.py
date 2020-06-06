from django.contrib import admin
from django.urls import path,include
from .import views
print("hh")
urlpatterns = [
    path('',views.registerForm),
    path('HH',views.hh),
]