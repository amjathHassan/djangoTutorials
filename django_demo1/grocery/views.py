from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
# Create your views here.

list_items = {
    "rice" : "Rice section",
    "sugar" : "Sugar section",
    "salt" : "Salt section",
}

def grocery(request):
    try:
        return HttpResponse("Select grocery items")
    except:
        return HttpResponseNotFound("Page not found")
# def rice(request):
#     return HttpResponse("Rice section")

# def sugar(request):
#     return HttpResponse("Sugar section")

# def salt(request):
#     return HttpResponse("Salt section")

def display_items(request, topic):
    
    try:
        return HttpResponse(list_items[topic])
    except:
        return render(request, '404.html', status= 404)
        return HttpResponseNotFound(f"{topic} not found")

def page_number(request, page_no):
    try:
        list_key_grocery = list(list_items.keys())
        topic = list_key_grocery[page_no]

        # return HttpResponse(list_items[topic])
        return HttpResponseRedirect(reverse('grocery:grocery', args= [topic]))
    except:
        return HttpResponseNotFound("not found grocery")