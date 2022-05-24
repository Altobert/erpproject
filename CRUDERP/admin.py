from django.contrib import admin

from .models import Producto, ProductoReceta, Receta, Stock

# Se va registrando el modelo dentro del administrador.

admin.site.register(Producto)
admin.site.register(ProductoReceta)
admin.site.register(Receta)
admin.site.register(Stock)


