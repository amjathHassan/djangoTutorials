from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

# Create your views here.

def home_page(request):
    return render(request, 'moviepage/home_page.html')
    pass

def custom_page_not_found(request, exception):
    return render(request, '404.html', status = 404)