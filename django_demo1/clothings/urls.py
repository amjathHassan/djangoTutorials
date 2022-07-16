from django.urls import path
from . import views

app_name = 'clothings'

urlpatterns = [
    path("", views.clothings),
    # path("kids/", views.kids),
    # path("men", views.men),
    # path("women", views.women),

    path("<int:page_no>/", views.page_num),
    path("<str:topic>/", views.display_items, name= 'clothings'),
    path("kids/", views.kids, name= 'kids'),
    path("men/", views.men, name= 'men'),
    path("women/", views.women, name= 'women'),

]

handler404 = "e_commerse.views.my_custom_page_not_found_view"
