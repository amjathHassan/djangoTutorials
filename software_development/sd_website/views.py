


from django.shortcuts import render


def main_home_page(request):
    return render(request, 'sd_website/main_home_page.html')
