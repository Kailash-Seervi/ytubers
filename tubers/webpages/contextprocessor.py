from .models import SiteHeader, SiteFooter


def setheader(request):
    header_obj=SiteHeader.objects.first()
    return {'header_obj':header_obj}

def setfooter(request):
    footer_obj=SiteFooter.objects.first()
    return {'footer_obj':footer_obj}
