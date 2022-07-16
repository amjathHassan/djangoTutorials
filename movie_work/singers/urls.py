
from . import views
from django.urls import path

app_name = 'singers'

urlpatterns = [
  
    path("", views.singers_home_page, name= 'singers_list_page'),
    path("actors/", views.actors_page, name= 'actors_path'),
    path("<int:page_no>/", views.page_number),
    path("<str:topic>/", views.display_singer, name='singer'),
    path("shreyaghoshal/", views.shreyaghoshal, name='shreyaghoshal'),
    path("vijayyesudas/", views.vijayyesudas, name='vijayyesudas'),
    path("rajalakshmiabhiram/", views.rajalakshmiabhiram, name='rajalakshmiabhiram'),
]
