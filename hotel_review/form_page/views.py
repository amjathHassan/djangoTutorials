from django.shortcuts import redirect, render
from django.urls import reverse
from .forms import SignUpForm, FormModelFormDB
from .models import SignUpFormDB, ModelFormDB

# Create your views here.
def form_home_page(request):

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            # print(form.cleaned_data)
            # print(request.POST["first_name"])   # or use this method

            print(form.cleaned_data['first_name'])
            first_name = form.cleaned_data['first_name']
            last_name = request.POST["last_name"]
            email = form.cleaned_data['email']
            SignUpFormDB.objects.create(first_name = first_name, last_name = last_name, email = email)
            print(SignUpFormDB.objects.all())
            return redirect(reverse('form_page:message'))
    else:
        form = SignUpForm()
        # print(SignUpFormDB.objects.all())
        return render(request, 'form_page/form_page.html', context= {"form": form})

def message(request):
    
    return render(request, 'form_page/message.html')

def model_form(request):

    if request.method  == "POST":
        form = FormModelFormDB(request.POST)
        if form.is_valid():
            print(request.POST)
            first_name = request.POST["first_name"]
            last_name = request.POST["last_name"]
            age = request.POST["age"]
            ModelFormDB.objects.create(first_name = first_name, last_name = last_name, age = age)
            print(ModelFormDB.objects.all())
            data = ModelFormDB.objects.all()
            return redirect(reverse('form_page:model_form_data', args= [data]))
    else:
        print(ModelFormDB.objects.all())
        form = FormModelFormDB()
        return render(request, 'form_page/model_form.html', context={'form': form})

def model_form_data(request, data):
    
    return render(request, 'form_page/model_form_data.html', context= {'data': data})