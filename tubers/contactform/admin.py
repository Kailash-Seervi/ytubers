from django.contrib import admin
from .models import ContactForm

class ContactFormAdmin(admin.ModelAdmin):
    list_display=['full_name','email','company_name','subject']

admin.site.register(ContactForm, ContactFormAdmin)