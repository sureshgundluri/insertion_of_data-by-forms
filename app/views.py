

from django.shortcuts import render
from app.models import *
from django.http import HttpResponse

def insert_topic(request):
    if request.method=='POST':
        tp=request.POST['tp']
        T=Topic.objects.get_or_create(topic_name=tp)[0]
        T.save()
        return HttpResponse('topic inserted successfully')
    return render (request,'insert_topic.html')

def insert_webpage(request):
    if request.method=='POST':
        tp=request.POST['tp']
        na=request.POST['na']
        ur=request.POST['ur']
        T=Topic.objects.get_or_create(topic_name=tp)[0]
        T.save()
        N=Webpage.objects.get_or_create(topic_name=T,name=na,url=ur)[0]
        N.save()
        return HttpResponse('webpage inserted successfully')
    return render (request,'insert_webpage.html')

def insert_access(request):
    if request.method=='POST':
        na=request.POST['na']
        da=request.POST['da']
        N=Webpage.objects.get_or_create(name=na)[0]
        N.save()
        A=AccessRecords.objects.get_or_create(name=N,date=da)[0]
        A.save()
        return HttpResponse('accessrecords inserted successfully')
    return render(request,'insert_access.html')

