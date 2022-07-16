"""e_commerse URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from cgitb import handler
from . import views

# def home_page(request):
    
#     try:
#         return render(request, 'e_com/home.html')
#         return HttpResponse("hey, welcome")
#     except:
#         return HttpResponseNotFound("Server Issue")


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.home_page),
    path("electronics/", include("electronics.urls")),
    path("grocery/", include("grocery.urls")),
    path("clothings/", include("clothings.urls")),
    path("watches/", include("watches.urls")),
]

handler404 = "e_commerse.views.my_custom_page_not_found_view"

