#from unicodedata import name
from django.urls import path 
from . import views

urlpatterns = [
    path('',views.inicio, name='inicio'),
    path('producto',views.producto, name='producto'),
    path('productoReceta',views.productoReceta, name='productoReceta'),
    path('stock', views.stock, name='stock'),
    path('receta',views.receta, name='receta'),
]
