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

def my_image2(request):
    return render(request, 'myimage2.html')

def my_image3(request):
    return render(request, 'myimage3.html')

def my_image4(request):
    return render(request, 'myimage4.html')

def my_image5(request, imagename):
    my_image_name = str(imagename);
    my_image_name = my_image_name.lower();
    print(my_image_name)
    if my_image_name == "django":
        var = True
    elif my_image_name == "python":
        var = False
        
    my_dict = { "var" : var}
    return render(request,'myimage5.html', context=my_dict)

def my_form(request):
    return render(request, 'myform.html')

#for form backend 
def submit_my_form(request):
    my_dictionary = {
        "var1" :request.POST['mytext'],
        "var2" :request.POST['mytextarea'],
        "method" :request.method 
    }

    return JsonResponse(my_dictionary)
