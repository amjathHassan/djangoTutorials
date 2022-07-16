from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

# Create your views here.

singers_list = ["shreyaghoshal", "vijayyesudas", "rajalakshmiabhiram"]
def singers_home_page(request):
    return render(request, 'singers/singers_list.html')

def page_number(request, page_no):
    topic = singers_list[page_no]

    return HttpResponseRedirect(reverse('singers:singer', args= [topic]))
    pass


def display_singer(request, topic):
    return render(request, f'singers/{topic}.html')
    pass

def shreyaghoshal(request):
    return render(request, 'singers/shreyaghoshal.html')
    

def vijayyesudas(request):
    return render(request, 'singers/vijayyesudas.html')
    

def rajalakshmiabhiram(request):
    return render(request, 'singers/rajalakshmiabhiram.html')
    

def actors_page(request):
    return render(request, 'actors/actors_list.html')
    pass