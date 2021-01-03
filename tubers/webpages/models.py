from django.db import models
from ckeditor.fields import RichTextField

class Sliders(models.Model):
    headline = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    button_text = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='media/slider/%Y')
    created_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.headline

class Team(models.Model):
    first_name=models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    fb_link = models.CharField(max_length=255)
    insta_link = models.CharField(max_length=255)
    photo = models.ImageField(upload_to="media/team/%Y/")
    created_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.first_name

class SiteHeader(models.Model):
    email=models.CharField(max_length=100)
    contact_no=models.CharField(max_length=100)

    def __str__(self):
        return self.email

class SiteFooter(models.Model):
    fb_link=models.CharField(max_length=100)
    insta_link=models.CharField(max_length=100)
    twitter_link=models.CharField(max_length=100)
    youtube_link=models.CharField(max_length=100)

    def __str__(self):
        return self.fb_link or ''

class AboutUs_section_one(models.Model):
    para=RichTextField()

    def __str__(self):
        return self.para[:15] or ''