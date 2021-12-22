from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import datetime
from tutorial import models
# Create your views here.


def functionBasedView(request):
    """
        simple function based view example
    """
    now = datetime.datetime.now()
    html = "<html><body> Tutorial Test Page <br/> It is now %s.</body></html>" % now
    return HttpResponse(html)

def submit(request):

    print('RECEIVED REQUEST: ' + request.method)

    if request.method == 'POST':
        print('Hello')

    elif request.method == 'GET':
        print("ehe")
    # obj = models.Todo()
    # obj.title = request.GET('title')
    # obj.description = request.GET('description')
    # obj.priority = request.GET('priority')
    # obj.save()
    # mydictionary = {
    #     "alltodos" : models.Todo.objects.all()
    # }
    # return JsonResponse(mydictionary)
    return "ehe"