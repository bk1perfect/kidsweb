from django.contrib import admin
from django.urls import path

from kids import views

urlpatterns = [
    path("", views.index, name='kids'),
    path("color", views.color, name = 'color'),
    path("animal", views.animal, name='animal'),
    # path("contact", views.contact, name='contact')
]