from django.shortcuts import render
from django.http import HttpResponse

def homepage(request):
    return HttpResponse('Home page1')

def room(request):
    return HttpResponse('Room page')
