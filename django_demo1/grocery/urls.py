from django.urls import path
from . import views

app_name = 'grocery'

urlpatterns = [
    path("", views.grocery),
    # path("rice/", views.rice),
    # path("sugar/", views.sugar),
    # path("salt/", views.salt),
    path("<int:page_no>/", views.page_number),
    path("<str:topic>/", views.display_items, name= 'grocery'),

]

handler404 = "e_commerse.views.my_custom_page_not_found_view"