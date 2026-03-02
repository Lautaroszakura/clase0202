from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def saludar(request):
    return HttpResponse("Hola desde django")

def saludar_con_etiqueta(request):
    return HttpResponse("<h1>Este es el tiulo de la app</h1>")

def index(request):
    return render(request,"core/index.html",{"titulo":"Python-Django"})

def tirar_dado(request):
    from datetime import datetime
    from random import randint
    
    tiro_de_dado=randint(1,6)
    if tiro_de_dado == 6:
        mensaje=f"has tirado el dado y has obtenido {tiro_de_dado} Ganaste"
    else:
        mensaje=f"has tirado el dado y has obtenido {tiro_de_dado} Perdiste"
    datos = {
        "Titulo":"Tiro de dados",
        "mensaje":mensaje,
        "fecha":datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
    }
    return render(request,"core/tirar_dado.html",datos)

def notas(request):
    mis_notas=[10,7,4,6,8,8]
    return render(request,"core/notas.html",context={"notas":mis_notas})