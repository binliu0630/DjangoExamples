from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings

print()
# Create your views here.

def home(request):
    return HttpResponse("hello home!")

def overview(request):
    return HttpResponse("hello overview!")