from django.contrib import admin
from django.shortcuts import render
from django.urls import path
from . import views
from cgitb import handler

app_name = 'actors'

urlpatterns = [
   
    path("", views.actors_home_page, name= 'actors_list_page'),
    path("singers/", views.singers_page, name= 'singers_path'),
    path("<int:page_no>/", views.page_number),
    path("<str:topic>/", views.display_actor, name = "actor"),

    path("dulquersalman/", views.dulquer, name= 'dulquersalman'),
    path("soubinsahir/", views.soubin, name= 'soubinsahir'),
    path("nedumudivenu/", views.nedumudi, name= 'nedumudi venu'),
]

handler404 = 'moviepage.views.custom_page_not_found'