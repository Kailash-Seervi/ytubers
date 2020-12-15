from django.shortcuts import render, get_object_or_404
from .models import Youtuber



def youtubers(request):
    tubers = Youtuber.objects.order_by('-created_date')
    data = {
        'tubers': tubers,
    }
    return render(request,'youtubers/youtubers.html', data)

def youtubers_detail(request, id):
    tuber = get_object_or_404(Youtuber, pk=id)
    data = {
        'tuber': tuber,
    }
    return render(request,'youtubers/youtubers_detail.html',data)

def search(request):
    tubers = Youtuber.objects.order_by('-created_date')
    city_search=Youtuber.objects.values_list('city',flat=True).distinct()
    camera_type_search=Youtuber.objects.values_list('camera_type',flat=True).distinct()
    catergory_search = Youtuber.objects.values_list('category', flat=True).distinct()
    
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            tubers = tubers.filter(city__iexact=city)
            
    if 'camera_type' in request.GET:
        city = request.GET['camera_type']
        if city:
            tubers = tubers.filter(camera_type__iexact=city)
            
    if 'category' in request.GET:
        city = request.GET['category']
        if city:
            tubers=tubers.filter(category__iexact=city)

    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            tubers = tubers.filter(description__icontains=keyword)
    data = {
        'tuber': tubers,
        'city_search': city_search,
        'camera_type_search': camera_type_search,
        'catergory_search':catergory_search,
        
    }
    return render(request,'youtubers/search.html',data)
