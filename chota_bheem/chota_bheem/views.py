from django.shortcuts import render


def homepage(request):
    return render(request, 'chota_bheem/homepage.html')