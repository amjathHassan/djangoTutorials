from django.urls import path
from . import views

app_name = 'delete'

urlpatterns = [
    path("", views.delete,name= 'delete_page'),
    path("show/", views.show_list, name= 'show_list')
    
    
]
