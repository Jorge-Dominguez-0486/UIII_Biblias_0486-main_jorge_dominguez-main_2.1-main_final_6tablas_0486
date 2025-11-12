from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio_biblias, name='inicio_biblias'),
    
    # Rutas de ClienteGlobal
    path('clientes/', views.ver_clientes, name='ver_clientes'),
    path('clientes/agregar/', views.agregar_cliente, name='agregar_cliente'),
    path('clientes/actualizar/<int:id>/', views.actualizar_cliente, name='actualizar_cliente'),
    path('clientes/realizar_actualizacion/<int:id>/', views.realizar_actualizacion_cliente, name='realizar_actualizacion_cliente'),
    path('clientes/borrar/<int:id>/', views.borrar_cliente, name='borrar_cliente'),

    # Rutas de Pedido
    path('pedidos/', views.ver_pedidos, name='ver_pedidos'),
    path('pedidos/agregar/', views.agregar_pedido, name='agregar_pedido'),
    path('pedidos/actualizar/<int:id>/', views.actualizar_pedido, name='actualizar_pedido'),
    path('pedidos/realizar_actualizacion/<int:id>/', views.realizar_actualizacion_pedido, name='realizar_actualizacion_pedido'),
    path('pedidos/borrar/<int:id>/', views.borrar_pedido, name='borrar_pedido'),

    # Rutas de DetallePedido
    path('detalles/', views.ver_detalles, name='ver_detalles'),
    path('detalles/agregar/', views.agregar_detalle_pedido, name='agregar_detalle_pedido'),
    path('detalles/actualizar/<int:id>/', views.actualizar_detalle_pedido, name='actualizar_detalle_pedido'),
    path('detalles/realizar_actualizacion/<int:id>/', views.realizar_actualizacion_detalle_pedido, name='realizar_actualizacion_detalle_pedido'),
    path('detalles/borrar/<int:id>/', views.borrar_detalle_pedido, name='borrar_detalle_pedido'),
    
    # Rutas de EditorialProveedor
    path('editoriales/', views.ver_editoriales, name='ver_editoriales'),
    path('editoriales/agregar/', views.agregar_editorial, name='agregar_editorial'),
    path('editoriales/actualizar/<int:id>/', views.actualizar_editorial, name='actualizar_editorial'),
    path('editoriales/realizar_actualizacion/<int:id>/', views.realizar_actualizacion_editorial, name='realizar_actualizacion_editorial'),
    path('editoriales/borrar/<int:id>/', views.borrar_editorial, name='borrar_editorial'),

    # Rutas de ProductosGlobal
    path('productos/', views.ver_productos, name='ver_productos'),
    path('productos/agregar/', views.agregar_producto, name='agregar_producto'),
    path('productos/actualizar/<int:id>/', views.actualizar_producto, name='actualizar_producto'),
    path('productos/realizar_actualizacion/<int:id>/', views.realizar_actualizacion_producto, name='realizar_actualizacion_producto'),
    path('productos/borrar/<int:id>/', views.borrar_producto, name='borrar_producto'),
    
    # Rutas de Inventario
    path('inventarios/', views.ver_inventarios, name='ver_inventarios'),
    path('inventarios/agregar/', views.agregar_inventario, name='agregar_inventario'),
    path('inventarios/actualizar/<int:id>/', views.actualizar_inventario, name='actualizar_inventario'),
    path('inventarios/realizar_actualizacion/<int:id>/', views.realizar_actualizacion_inventario, name='realizar_actualizacion_inventario'),
    path('inventarios/borrar/<int:id>/', views.borrar_inventario, name='borrar_inventario'),
]