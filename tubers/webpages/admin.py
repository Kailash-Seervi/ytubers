from django.contrib import admin
from .models import Sliders,Team, SiteHeader, SiteFooter
from django.utils.html import format_html
class TeamAdmin(admin.ModelAdmin):
    def myphoto(self,object):
        return format_html("<img src='{}' width='40'/>".format(object.photo.url))
    
    
    list_display = ['id','myphoto', 'first_name', 'role', 'created_date']
    list_display_links = ['first_name', 'id']
    search_fields = ['first_name', 'role']
    list_filter=('role',)

class SliderAdmin(admin.ModelAdmin):
    def sliderphoto(self, object):
        return format_html("<img src='{}' width='100' height='40' />".format(object.photo.url))


    list_display=['headline', 'sliderphoto','button_text']

class SiteHeaderAdmin(admin.ModelAdmin):
    list_display=['email','contact_no']

class SiteFooterAdmin(admin.ModelAdmin):
    list_display=['fb_link','insta_link','twitter_link','youtube_link']

admin.site.register(Sliders, SliderAdmin)
admin.site.register(Team,TeamAdmin)
admin.site.register(SiteHeader, SiteHeaderAdmin)
admin.site.register(SiteFooter,SiteFooterAdmin)