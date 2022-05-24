from django.contrib import admin

from .models import ProductoReceta, Producto, Receta, Stock, UnidadMedida

# Se va registrando el modelo dentro del administrador.

admin.site.register(ProductoReceta)
admin.site.register(Producto)
admin.site.register(Receta)
admin.site.register(Stock)
admin.site.register(UnidadMedida)



