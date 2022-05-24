

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models  import Producto
  
# Create your views here.

def inicio(request):
    #return HttpResponse("<h1> Hola Mundo. Te encuentras en el inicio. </h1>")
     # render function takes argument  - request
    # and return HTML as response
    return render(request, "base.html")


def producto(request):
    return render(request, "producto.html")


def receta(request):
    return render(request, "receta.html")


def productoReceta(request):
    return render(request, "productoReceta.html")


def stock(request):
    return render(request, "stock.html")


def mostrarProducto(request):  
    employees = Employee.objects.all()  
    return render(request,"show.html",{'employees':employees})  