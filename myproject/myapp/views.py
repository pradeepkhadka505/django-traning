from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# Create your views here.

def onfunctioncall(request):
    return HttpResponse("hello new git poject")

def about_function(request):
    return HttpResponse("this is about ")

def add(request, a, b):
    return HttpResponse( a + b)

def intro(request, name, age):

    my_dict = {"name": name, "age": age}
    
    return JsonResponse(my_dict)

def myfirstpage(request):
    return render(request, 'index.html')

def mysecondpage(request):
    return render(request, 'second.html')

def mythirdpage(request):

    var = "Helloo world"
    name = "pradeep Khadka"
    greeting = "Hey, How R you ??"
    fruits = ["apple","banana", "orange", "pine-apple", "grapes"]
    num1, num2 = 100, 15
    ans = num1 > num2
    my_dict = {
        "var": var, 
        "name": name, 
        "msg" : greeting, 
        "myfruits" : fruits,
        "num1": num1, 
        "num2": num2, 
        "ans": ans}
    return render(request, 'third.html', my_dict)

def my_image(request):
    return render(request, 'myimage.html')
    
