"""library URL Configuration

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
from django import urls
from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView
from . import views

app_name = 'catalog'

urlpatterns = [ 
    path("", views.index, name= 'index'),
    path('create_book/', views.BookCreate.as_view(), name = 'create_book'),
    path('book_details/<int:pk>/', views.BookDetail.as_view(), name = 'book_details'),
    path('create_author/', views.AuthorCreate.as_view(), name= 'create_author'),
    path('author_details/<int:pk>/', views.AuthorDetail.as_view(), name = 'author_detail'),
    path('create_genre/', views.GenreCreate.as_view(), name = 'create_genre'),
    path('genre_details/<int:pk>/', views.GenreDetail.as_view(), name = 'genre_detail'),
    path('create_language/', views.LanguageCreate.as_view(), name= 'create_language'),
    path('language_details/<int:pk>/', views.LanguageDetail.as_view(), name= 'language_detail'),
    
    path('my_view/', views.my_view, name = 'my_view'),
    path('signup/', views.SignUpView.as_view(), name = 'signup'),
    path('profile/', views.CheckedOutByUserView.as_view(), name = 'profile'),
    
]
