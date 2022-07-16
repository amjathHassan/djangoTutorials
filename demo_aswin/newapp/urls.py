from django.urls import path
from . import views

urlpatterns = [
    path("", views.section_new_app),
    # path("<int:page_no1>/""<int:page_no2>/", views.page_no),
    path("<int:page_no>/", views.page_number),
    path("<topic>/", views.show_page, name= "contents"),
    
    # path("phone/", views.phone),
    # path("tv/", views.tv),
    # path("laptop/", views.laptop),
]