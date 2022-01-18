from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View

class TestView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "app/index.html")