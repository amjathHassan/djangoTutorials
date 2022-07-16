from django.urls import path
from .  import views

urlpatterns = [
    path("", views.sections),
    path("sports/", views.sports),
    path("arts/", views.arts),
]