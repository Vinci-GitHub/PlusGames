from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.views.generic import TemplateView

def index(request: HttpRequest):
    return render(request, 'index.html')

