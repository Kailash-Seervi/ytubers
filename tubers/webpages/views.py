from django.shortcuts import render
from .models import Sliders, Team
from youtubers.models import Youtuber
from webpages.models import AboutUs_section_one

def home(request):
    sliders = Sliders.objects.all()
    teams=Team.objects.all()
    featured_youtubers=Youtuber.objects.order_by('-created_date').filter(is_featured=True)
    data = {
        'sliders':sliders,
        'teams': teams,
        'featured_youtubers':featured_youtubers,
    }
    return render(request, 'webpages/home.html', data)

def about(request):
    teams=Team.objects.all()
    aboutus=AboutUs_section_one.objects.first()
    data={
        'teams':teams,
        'aboutus_para': aboutus,
    }
    return render(request, 'webpages/about.html',data)

def services(request):
    return render(request, 'webpages/services.html')

def contact(request):
        return render(request, 'webpages/contact.html')