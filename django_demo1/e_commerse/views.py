from django.shortcuts import render
from django.http import HttpResponseNotFound

def home_page(request):
    
    
    return render(request, 'e_com/home.html')
    

def my_custom_page_not_found_view(request, exception):
    return render(request, "404.html", status= 404)