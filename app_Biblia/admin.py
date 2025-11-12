from django.contrib import admin
from .models import (
    ClienteGlobal, 
    Pedido, 
    EditorialProveedor, 
    ProductosGlobal, 
    Inventario, 
    DetallePedido
)

admin.site.register(ClienteGlobal)
admin.site.register(Pedido)
admin.site.register(EditorialProveedor)
admin.site.register(ProductosGlobal)
admin.site.register(Inventario)
admin.site.register(DetallePedido)