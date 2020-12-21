from django.shortcuts import redirect, render
from .models import Hiretubers
# first_name=models.CharField(max_length=100)
# last_name=models.CharField(max_length=100)
# tuber_id=models.IntegerField()
# tuber_name=models.CharField(max_length=100)
# email=models.EmailField(blank=True)
# city=models.CharField(max_length=100)
# phone=models.CharField(max_length=100)
# state=models.CharField(max_length=100)
# message=models.TextField(blank=True)
# user_id=models.IntegerField(blank=True)

def hiretuber(request):
    if request.method=='POST':
        first_name=request.POST['last_name']
        last_name=request.POST['last_name']
        tuber_id=request.POST['last_name']
        tuber_name=request.POST['last_name']
        email=request.POST['last_name']
        city=request.POST['last_name']
        phone=request.POST['last_name']
        state=request.POST['last_name']
        message=request.POST['last_name']
        user_id=request.POST['last_name']

        hiretuber=Hiretubers(first_name=first_name,last_name=last_name,tuber_id=tuber_id,tuber_name=tuber_name,email=email,city=city,phone=phone,state=state, message=message,user_id=user_id)

        hiretuber.save()
        message.success(request, 'Thanks for reaching out!')
        return redirect('youtubers')
