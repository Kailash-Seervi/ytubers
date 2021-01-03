from django.db import models
from datetime import datetime


class ContactForm(models.Model):
    full_name=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    email=models.CharField(max_length=100,blank=True)
    company_name=models.CharField(max_length=100)
    subject=models.CharField(max_length=100)
    message=models.TextField(blank=True)
    user_id=models.IntegerField(blank=True)
    created_date=models.DateTimeField(blank=True, default=datetime.now())

    def __str__(self):
        return self.email