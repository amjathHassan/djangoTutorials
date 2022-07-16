from django.urls import path
from . import views

app_name = 'electronics'

urlpatterns = [
    path("", views.electronics),
    # path("phone/", views.phone),
    # path("laptop/", views.laptop),
    # path("tv/", views.tv),
    path("<int:page_no>/", views.page_number),
    path("<str:topic>/", views.display_items, name= 'electronics'),
]


