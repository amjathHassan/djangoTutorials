from django.shortcuts import render
from django.http import Http404, HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse



# Create your views here.

list_of_items = {
    "rado" : "Rado Section",
    "titan" : "Titan Section",
    "gshock" : "G-Shock Section",
    
}



def watches(request):
    # my_var = {
    #         'firstname' : "Fahad",
    #         'age' : 43,
    #         "list_items": [1, 2, 3, 4, 5],
    #     }

    #     # return HttpResponse("Select Watch Brand")     # normal return of http response
    # return render(request, 'watches/conventional.html', context= my_var)     # rendering a html template
    try:
        my_var = {
            'firstname' : "Fahad",
            'age' : 43,
            "list_items": [1, 2, 3, 4, 5],
        }

        # return HttpResponse("Select Watch Brand")     # normal return of http response
        return render(request, 'watches/conventional.html', context= my_var)     # rendering a html template

    except:

        return HttpResponseNotFound("Page not found")

# def rado(request):
#     return HttpResponse(list_of_items["rado"])
# def titan(request):
#     return HttpResponse(list_of_items["titan"])
# def gshock(request):
#     return HttpResponse(list_of_items["gshock"])
# def display_func(request,topic):
#     if topic in search_words_keys:
#         return HttpResponse(list_of_items[topic])
#     else:
#         return HttpResponseNotFound(f"{topic} not found")


def display_func(request,topic):
    
    try:
        
        return HttpResponse(list_of_items[topic])
    except:
        return render(request, "404.html", status= 404)
        # return HttpResponseNotFound(f"{topic} page not found")

# def sum_disp(request, num1, num2):
#     result = num1 + num2
#     return HttpResponse(result)

def page_number(request, page_no):
    # search_list_key = list(list_of_items.keys())
    # topic = search_list_key[page_no]
    # return HttpResponseRedirect(reverse("watches", args= [topic]))
    
    try:
        search_list_key = list(list_of_items.keys())
        topic = search_list_key[page_no]
        # return HttpResponse(list_of_items[topic])
        return HttpResponseRedirect(reverse("watches:watches", args= [topic]))
    except:
        # return HttpResponseNotFound("Page Not Found")
        raise Http404("No Page Found")
    
def offer_page(request):
    offer_status = {
        'status' : "Offers are not available"
    }
    return render(request, 'watches/offers.html', context= offer_status)
    pass


