from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

# Create your views here.

actors_list = ["dulquersalman", "soubinsahir", "nedumudivenu"]

def actors_home_page(request):
    return render(request, 'actors/actors_list.html')
    pass

def page_number(request, page_no):
    topic = actors_list[page_no]
    return HttpResponseRedirect(reverse('actors:actor', args= [topic]))

    pass
def display_actor(request, topic):
    return render(request, f"actors/{topic}.html")

def singers_page(request):
    return render(request, 'singers/singers_list.html')
    pass


def dulquer(request):
    return render(request, 'actors/dulquersalman.html')
def soubin(request):
    return render(request, 'actors/soubinsahir.html')
def nedumudi(request):
    return render(request, 'actors/nedumudivenu.html')

def custom_page_not_found(request, exception):
    return render(request, 'actors/404.html', status = 404)