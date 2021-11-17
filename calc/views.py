from django.shortcuts import render
from django.http import HttpResponse, JsonResponse


def say_hello(request):
    return HttpResponse("Hello World!")



def add(request, num1, num2):
    print(f"Add: {num1, num2}")
    sum = num1 + num2
    return HttpResponse(sum)
