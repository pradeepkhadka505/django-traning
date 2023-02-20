from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# Create your views here.

def onfunctioncall(request):
    return HttpResponse("hello new git poject")

def about_function(request):
    return HttpResponse("this is about ")