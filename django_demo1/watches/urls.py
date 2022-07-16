from django.urls import path
from . import views

app_name = 'watches'

urlpatterns = [
    path("", views.watches),
    path("offers/", views.offer_page, name= 'offers_page'), 
    # path("<int:num1>/""<int:num2>/", views.sum_disp),
    path("<int:page_no>/", views.page_number),
    path("<str:topic>/", views.display_func, name= 'watches'),
    # path("rado/", views.rado),
    # path("titan/", views.titan),
    # path("gshock/", views.gshock),

]

handler404 = "e_commerse.views.my_custom_page_not_found_view"
