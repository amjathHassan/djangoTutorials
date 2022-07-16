
from unicodedata import name
from django.contrib import admin
from django.urls import path
from . import views

app_name = 'form_page'


urlpatterns = [
    path("", views.form_home_page, name="form_page"),
    path("message/", views.message, name= 'message'),
    path("modelform/", views.model_form, name = "model_form"),
    path("modelformdata/<data>", views.model_form_data, name = "model_form_data"),
]
