from django.shortcuts import render
from .models import Sliders, Team

def home(request):
    sliders = Sliders.objects.all()
    teams=Team.objects.all()
    data = {
        'sliders':sliders,
        'teams':teams
    }
    return render(request, 'webpages/home.html', data)

def about(request):
    return render(request, 'webpages/about.html')

def services(request):
    return render(request, 'webpages/services.html')

def contact(request):
        return render(request, 'webpages/contact.html')