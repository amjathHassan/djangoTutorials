from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def sections(request):
    return HttpResponse("Please type the section you want to go to")

def sports(request):
    return HttpResponse("Welcome to sports page")

def arts(request):
    return HttpResponse("Welcome to arts page")
