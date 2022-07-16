from django.shortcuts import render
from django.http import Http404, HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here.

list_items = {
    "kids" : "Kid's Section",
    "men" : "Mens's Section",
    "women" : "women's Section",
}

def clothings(request):
    try:
        return render(request, 'clothings/conventional.html')
        return HttpResponse("Select Your Section")
    except:
        return HttpResponseNotFound("NO page found")
def kids(request):

    return render(request, 'clothings/kids.html')
    return HttpResponse()

def men(request):
    return render(request, 'clothings/men.html')
    return HttpResponse("Men's Section")

def women(request):
    return render(request, 'clothings/women.html')
    return HttpResponse("women's Section")

def display_items(request, topic):
    try:
        return render(request, f'clothings/{topic}.html')
        return HttpResponse(list_items[topic])
    except:
        return render(request, "404.html", status= 404)
        return HttpResponseNotFound(f"{topic} page not found")

def page_num(request, page_no):
    try:
        list_items_keys = list(list_items.keys())
        topic = list_items_keys[page_no]

        
        return HttpResponseRedirect(reverse("clothings:clothings", args = [topic]))
    except:
        raise Http404("Page not found")