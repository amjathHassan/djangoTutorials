from django.http import Http404, HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

# Create your views here.

articles = {
    "phone" : "this is PHONE section",
    "tv" : "this is TV section",
    "laptop" : "this is LAPTOP section"
}

def section_new_app(request):
    return render(request, 'newapp/ele_homepage.html')
    return HttpResponse("this is electronics section")

def show_page(request, topic):
    try:
        return HttpResponse(articles[topic])
    except:
        raise Http404("not found")
        return HttpResponseNotFound("this page is not available not found")

    pass

def page_number(request, page_no):
    list_keys = list(articles.keys())
    topic = list_keys[page_no]
    return HttpResponseRedirect(reverse("contents", args= [topic]))
    return HttpResponse(articles[topic])


# def page_no(request, page_no1, page_no2):
#     return HttpResponse(page_no1 + page_no2)


# def phone(request):
#     return HttpResponse(articles["phone"])

# def tv(request):
#     return HttpResponse(articles["tv"])

# def laptop(request):
#     return HttpResponse(articles["laptop"])