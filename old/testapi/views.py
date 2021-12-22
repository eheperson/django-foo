from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import datetime

# Create your views here.


def test(request):

    if request.method == 'GET':
        now = datetime.datetime.now()
        html = "<html><body>It is now %s.</body></html>" % now
        # request.session['my_car'] = 'mini'
        return HttpResponse(request.session.id)

    if request.method == 'POST':
        return HttpResponse("ehe")