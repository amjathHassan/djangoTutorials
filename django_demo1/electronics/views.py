from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here.

list_items = {
    "phone" : "This phone section",
    "laptop" : "This laptop section",
    "tv" : "This tv section",
}

def electronics(request):
    try:
        return render(request, 'electronics/conventional.html')
        return HttpResponse("This electronics section")
    except:
        return HttpResponseNotFound("Page not found")
# def phone(request):
#     return HttpResponse("This phone section")

# def laptop(request):
#     return HttpResponse("This laptop section")

# def tv(request):
#     return HttpResponse("This tv section")

def display_items(request, topic):
    try:
        return HttpResponse(list_items[topic])
    except:
        
        return HttpResponseNotFound(f"{topic} not found")
        
def page_number(request, page_no):
    try:
        list_keys_dict = list(list_items.keys())
        topic = list_keys_dict[page_no]
        return HttpResponseRedirect(reverse('electronics:electronics', args= [topic]))
    except:
        return HttpResponseNotFound("Not found electronics")

    pass
