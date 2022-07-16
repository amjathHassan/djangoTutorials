from django.shortcuts import render


def home_page(request):
    
    return render(request, 'site_1/welcome.html') 
    return HttpResponse("<h1> Home Page</h1>")

def my_custom_page_not_found_view(request, exception):
    return render(request, '404.html', status= 404)
    pass