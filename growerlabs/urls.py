
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
   
    path('', views.home, name='home'),
    path('contact', views.contact, name="contact"),
    path('about', views.about, name="about"),
    path('projects', views.projects, name="projects"),
    path('profile/<int:pk>', views.profile, name="profile"),
    path("services", views.services, name="services"),
]