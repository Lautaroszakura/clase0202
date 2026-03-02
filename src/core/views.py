from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def saludar(request):
    return HttpResponse("Hola desde django")

def saludar_con_etiqueta(request):
    return HttpResponse("<h1>Este es el tiulo de la app</h1>")

def index(request):
    return render(request,"core/index.html")