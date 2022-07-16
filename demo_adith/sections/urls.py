from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


app_name = 'sections'

urlpatterns = [
    path("", views.sections_1),

    path('image_upload/', views.hotel_image_view, name = 'image_upload'),
    path('success/', views.success, name = 'success'),
    
    path("model/", views.model_func, name = "model_page"),
    path("form1/", views.review, name= "review"),
    path("thankyou/", views.thankyou, name = "thankyou"),
   
    # path("<int:num1>/""<int:num2>/", views.sum),
    path("<int:page_no>/", views.page_number),
    path("<str:topic>/", views.disp_func, name= 'section'),
    
    
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)