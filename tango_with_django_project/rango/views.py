# Create your views here.

from django.http import HttpResponse

def index(request):
    return HttpResponse("Rango say Hello World! <a href='/rango/about'>About</a>")

def about(request):
    return HttpResponse("Rango say here is the about page <a href='/rango/'>index</a>")