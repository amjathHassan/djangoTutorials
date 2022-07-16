from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def section2(request):
    return render(request, 'sample1/hello.html')
    return HttpResponse("<h1>Hello World</h2>")
