from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("Hello world home chai or django")
    return render(request, 'index.html')
def about(request):
    return render(request, 'about.html')

def contact(request):
    return HttpResponse("Hello world contact chai or django")
