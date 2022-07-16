from django.http import Http404, HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from . import models
from .forms import ReviewForm

# Create your views here.

section_items = {
    'sports' : "Sports page",
    'news' : "news page",
}

def sections_1(request):
    try:
        my_var = {
            'firstname' : "Ajith",
            'age' : 34,
            "response" : "this is section page"
        }
        return render(request, 'welcome.html', context= my_var)
        return HttpResponse("sections page")
        
    except:
        raise Http404("page not found")
        return HttpResponseNotFound("page not found")

# def sum(request, num1, num2):
#     result = num1 + num2
#     return HttpResponse(result)

def page_number(request, page_no):
    try:
        list_key_dict = list(section_items.keys())
        topic = list_key_dict[page_no]
        # return HttpResponse(section_items[topic])

        return HttpResponseRedirect(reverse('section', args = [topic]))
    except:

        raise Http404("Page Not Found")

        return HttpResponseNotFound("not found")

def disp_func(request, topic):
    try:
        return HttpResponse(section_items[topic])
    except:
        return HttpResponseNotFound("not found")

def model_func(request):
    all_patients = models.Patients.objects.all()
    patient_list = {"patients": all_patients}
    return render(request, 'model_page.html', context= patient_list)
    pass


def review(request):

    if request.method == "POST":
        form  = ReviewForm(request.POST)
        if form.is_valid():
            print(request.POST)
            return render(request, 'sections/thankyou.html')
    else:
        form = ReviewForm()
    return render(request, "sections/form1.html", context= {"form": form})
    pass

def thankyou(request):
    return render(request, 'sections/thankyou.html')
    pass


from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import *

# Create your views here.
def hotel_image_view(request):

	if request.method == 'POST':
		form = HotelForm(request.POST, request.FILES)

		if form.is_valid():
			form.save()
			return redirect('sections:success')
	else:
		form = HotelForm()
	return render(request, 'hotel_image_form.html', {'form' : form})


def success(request):
	return HttpResponse('successfully uploaded')
