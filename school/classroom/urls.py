"""school URL Configuration

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
from django.urls import path
from .views import HomeView, ContactFormView, ThankYouView, TeacherCreateView, TeacherListView, TeacherUpdateView, TeacherDeleteView, TeacherDetailView

app_name = 'classroom'

urlpatterns = [
    # path("", views.homepage, name="homepage"),

    path("", HomeView.as_view(), name="homepage"),
    path('contact/', ContactFormView.as_view(), name = 'contact'),
    path('thank_you/', ThankYouView.as_view(), name = 'thank_you'),
    path('create_teacher/', TeacherCreateView.as_view(), name = 'create_teacher'),

    path('list_teacher/', TeacherListView.as_view(), name= 'list_teacher'),
    path('update_teacher/<int:pk>/', TeacherUpdateView.as_view(), name= 'update_teacher'),
    path('delete_teacher/<int:pk>/', TeacherDeleteView.as_view(), name= 'delete_teacher'),
    path('detail_teacher/<int:pk>/', TeacherDetailView.as_view(), name='detail_teacher'),


]
