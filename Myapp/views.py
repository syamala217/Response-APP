from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

def homePageView(request):
    json = {"Message": "Hello World!"}
    return JsonResponse(json)