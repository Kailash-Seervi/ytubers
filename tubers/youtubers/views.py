from django.shortcuts import render, get_object_or_404
from .models import Youtuber



def youtubers(request):
    tubers = Youtuber.objects.order_by('-created_date')
    cities=Youtuber.objects.values_list('city',flat=True).all().distinct()
    camera_types=[ x[0]  for x in Youtuber.camera_choices ]
    categories=[ x[0]  for x in Youtuber.category_choices ] 
    data = {
        'tubers': tubers,
        'cities': cities,
        'camera_types': camera_types,
        'categories': categories,
    }
    return render(request,'youtubers/youtubers.html', data)

def youtubers_detail(request, id):
    tuber = get_object_or_404(Youtuber, pk=id)
    data = {
        'tuber': tuber,
    }
    return render(request,'youtubers/youtuber_detail.html',data)

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
        camera_type = request.GET['camera_type']
        if camera_type:
            tubers = tubers.filter(camera_type__iexact=camera_type)
            
    if 'category' in request.GET:
        category = request.GET['category']
        if category:
            tubers=tubers.filter(category__iexact=category)

    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            tubers = tubers.filter(description__icontains=keyword)
    data = {
        'tubers': tubers,
        'city_search': city_search,
        'camera_type_search': camera_type_search,
        'catergory_search':catergory_search,
        
    }
    return render(request,'youtubers/search.html',data)
