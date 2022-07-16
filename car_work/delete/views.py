from django.shortcuts import redirect, render
from django.urls import reverse
from .forms import DeleteForm
from create.models import CarListDB

# Create your views here.
def delete(request):
    if request.method == "POST":
        form = DeleteForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            delete_item = request.POST['brand_name']
            # print(CarListDB.objects.all())
            CarListDB.objects.filter(brand_name = delete_item).delete()
            print(CarListDB.objects.all())
            return redirect(reverse('delete:show_list'))
    else:
        form = DeleteForm()
        return render(request, 'delete/delete_page.html', context={'form': form})
    pass

def show_list(request):
    db_list = CarListDB.objects.all()
    return render(request, 'delete/show_list.html', context= {'db_list': db_list})