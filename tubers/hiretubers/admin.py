from django.contrib import admin
from .models import Hiretubers

admin.site.register(Hiretubers)

class HiretubersAdmin(admin.ModelAdmin):
    list_display=['first_name','tuber_name','created_date']
