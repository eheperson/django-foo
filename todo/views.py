from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import datetime
from .models import *
# Create your views here.



def elo(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)


def submit(request):
    obj = Todo()
    obj.title = request.GET['title']
    obj.description = request.GET['description']
    obj.priority = request.GET['priority']  
    obj.save()
    mydictionary = {
        "alltodos" : Todo.objects.all()
    }
    return JsonResponse(mydictionary)

def delete(request,id):
    obj = Todo.objects.get(id=id)
    obj.delete()
    mydictionary = {
        "alltodos" : Todo.objects.all()
    }
    return render(request,'list.html',context=mydictionary)

def list(request):
    mydictionary = {
        "alltodos" : Todo.objects.all()
    }
    return HttpResponse(mydictionary)

def sortdata(request):
    mydictionary ={
        "alltodos" : Todo.objects.all().order_by('-priority')
    }
    return render(request,'list.html',context=mydictionary)

def searchdata(request):
    q = request.GET['query']
    mydictionary = {
        "alltodos" : Todo.objects.filter(title__contains=q)
    }
    return render(request,'list.html',context=mydictionary)

def edit(request,id):
    obj = Todo.objects.get(id=id)
    mydictionary = {
        "title" : obj.title,
        "description" : obj.description,
        "priority" : obj.priority,
        "id" : obj.id
    }
    return render(request,'edit.html',context=mydictionary)


def update(request,id):
    obj = Todo(id=id)
    obj.title = request.GET['title']
    obj.description = request.GET['description']
    obj.priority = request.GET['priority']
    import datetime
    updated_at = datetime.datetime.now()
    obj.created_at = updated_at
    obj.save()
    mydictionary = {
        "alltodos" : Todo.objects.all()
    }
    return render(request,'list.html',context=mydictionary)


