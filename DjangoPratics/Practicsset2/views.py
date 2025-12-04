from django.shortcuts import render
form django.http import HttpResponse
# Create your views here.
def practicsset2_home(request):
    return httpResponse("Welcome to Practicsset2 Home Page")
    # return render(request, 'Practicsset2/practicsset2_home.html')