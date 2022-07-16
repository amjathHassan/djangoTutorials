
from django.urls import path
from . import views

app_name = 'read'

urlpatterns = [
    path("", views.show_db, name= 'show_db'),
   
    
]
