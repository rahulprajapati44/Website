from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
    #return HttpResponse("Hello World")
    #return render(request,"home.html")  # we are rendering html page, this one is static below statement make is dynamic
    return render(request,"home.html",{"name":"Rahul"}) # it is dynamic now because we are not changing name i html file

def add(request):
    value1 = request.POST["num1"]  # to get value from user input which is stored as num1
    value2 = request.POST["num2"]  # to get value from user input which is stored as num2
    res = int(value1)+int(value2)
    return render(request, "result.html",{"operation":"Addition","result":res}) # sending value to the html

def mul(request):
    value1 = request.POST["num3"]
    value2 = request.POST["num4"]
    res = int(value1)*int(value2)
    return render(request,"result.html",{"operation":"Multiplication","result":res})