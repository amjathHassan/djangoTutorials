from django.shortcuts import render
from create.models import CarListDB

# Create your views here.
def show_db(request):
    db_list = CarListDB.objects.all()
    return render(request, 'read/show_db.html', context= {'db_list': db_list})
