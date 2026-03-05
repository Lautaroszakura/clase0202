from django.shortcuts import render
#. porque models esta a la misma altura que views
from . import models

# Create your views here.

def producto_list(request):
    #Se importa el modelo
    productos=models.Categoria.objects.all()
    return render(request, "producto/producto_list.html", {"productos":productos})