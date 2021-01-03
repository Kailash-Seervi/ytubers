from django.contrib import admin
from .models import Hiretubers

class HiretubersAdmin(admin.ModelAdmin):
    list_display=['first_name', 'email','tuber_name','created_date']

admin.site.register(Hiretubers, HiretubersAdmin)
