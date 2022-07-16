from django.shortcuts import redirect, render
from django.urls import reverse
from .forms import CarListCreate
from .models import CarListDB

# Create your views here.
def create(request):

    if request.method == "POST":
        form = CarListCreate(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            car_name = request.POST['car_name']
            brand_name = request.POST['brand_name']
            CarListDB.objects.create(car_name = car_name, brand_name = brand_name)
            print(CarListDB.objects.all())
            return redirect(reverse('create:status'))
    else:
        form = CarListCreate()
        # print(CarListDB.objects.all())
        return render(request, 'create/create_page.html', context= {'form': form})

def status(request):
    return render(request, 'create/submit_result.html')

