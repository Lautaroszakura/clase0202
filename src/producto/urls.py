from django.urls import path

from producto import views

urlpatterns = [
    path("lista/",views.producto_list, name="lista"),
]