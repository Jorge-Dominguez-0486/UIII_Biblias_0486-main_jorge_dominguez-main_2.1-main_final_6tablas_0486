from django.shortcuts import render, redirect, get_object_or_404
from .models import (
    ClienteGlobal, 
    Pedido, 
    EditorialProveedor, 
    ProductosGlobal, 
    Inventario, 
    DetallePedido
)

def inicio_biblias(request):
    return render(request, 'inicio.html')

# ===================
# VISTAS: CLIENTE GLOBAL (8 campos)
# ===================
def ver_clientes(request):
    clientes = ClienteGlobal.objects.all()
    return render(request, 'cliente/ver_clientes.html', {'clientes': clientes})

def agregar_cliente(request):
    if request.method == 'POST':
        ClienteGlobal.objects.create(
            nombre=request.POST.get('nombre'),
            apellido=request.POST.get('apellido'),
            email=request.POST.get('email'),
            fecha_nacimiento=request.POST.get('fecha_nacimiento') or None,
            pais_residencia=request.POST.get('pais_residencia'),
            codigo_postal=request.POST.get('codigo_postal'),
            telefono=request.POST.get('telefono')
        )
        return redirect('ver_clientes')
    return render(request, 'cliente/agregar_cliente.html')

def actualizar_cliente(request, id):
    cliente = get_object_or_404(ClienteGlobal, id=id)
    return render(request, 'cliente/actualizar_cliente.html', {'cliente': cliente})

def realizar_actualizacion_cliente(request, id):
    cliente = get_object_or_404(ClienteGlobal, id=id)
    if request.method == 'POST':
        cliente.nombre = request.POST.get('nombre')
        cliente.apellido = request.POST.get('apellido')
        cliente.email = request.POST.get('email')
        cliente.fecha_nacimiento = request.POST.get('fecha_nacimiento') or None
        cliente.pais_residencia = request.POST.get('pais_residencia')
        cliente.codigo_postal = request.POST.get('codigo_postal')
        cliente.telefono = request.POST.get('telefono')
        cliente.save()
        return redirect('ver_clientes')
    return render(request, 'cliente/actualizar_cliente.html', {'cliente': cliente})

def borrar_cliente(request, id):
    cliente = get_object_or_404(ClienteGlobal, id=id)
    if request.method == 'POST':
        cliente.delete()
        return redirect('ver_clientes')
    return render(request, 'cliente/borrar_cliente.html', {'cliente': cliente})

# ===================
# VISTAS: PEDIDO (9 campos)
# ===================
def ver_pedidos(request):
    pedidos = Pedido.objects.all().order_by('-fecha_hora')
    return render(request, 'pedido/ver_pedidos.html', {'pedidos': pedidos})

def agregar_pedido(request):
    clientes = ClienteGlobal.objects.all() 
    if request.method == 'POST':
        cliente_obj = get_object_or_404(ClienteGlobal, id=request.POST.get('cliente'))
        Pedido.objects.create(
            cliente=cliente_obj,
            total_neto=request.POST.get('total_neto', 0),
            metodo_pago=request.POST.get('metodo_pago'),
            estado_pedido=request.POST.get('estado_pedido', 'Pendiente'),
            impuesto_total=request.POST.get('impuesto_total', 0),
            costo_envio=request.POST.get('costo_envio', 0),
            direccion_envio=request.POST.get('direccion_envio')
        )
        return redirect('ver_pedidos')
    return render(request, 'pedido/agregar_pedido.html', {'clientes': clientes})

def actualizar_pedido(request, id):
    pedido = get_object_or_404(Pedido, id=id)
    clientes = ClienteGlobal.objects.all()
    context = {'pedido': pedido, 'clientes': clientes}
    return render(request, 'pedido/actualizar_pedido.html', context)

def realizar_actualizacion_pedido(request, id):
    pedido = get_object_or_404(Pedido, id=id)
    if request.method == 'POST':
        pedido.cliente = get_object_or_404(ClienteGlobal, id=request.POST.get('cliente'))
        pedido.total_neto = request.POST.get('total_neto')
        pedido.metodo_pago = request.POST.get('metodo_pago')
        pedido.estado_pedido = request.POST.get('estado_pedido')
        pedido.impuesto_total = request.POST.get('impuesto_total')
        pedido.costo_envio = request.POST.get('costo_envio')
        pedido.direccion_envio = request.POST.get('direccion_envio')
        pedido.save()
        return redirect('ver_pedidos')
    clientes = ClienteGlobal.objects.all()
    return render(request, 'pedido/actualizar_pedido.html', {'pedido': pedido, 'clientes': clientes})

def borrar_pedido(request, id):
    pedido = get_object_or_404(Pedido, id=id)
    if request.method == 'POST':
        pedido.delete()
        return redirect('ver_pedidos')
    return render(request, 'pedido/borrar_pedido.html', {'pedido': pedido})

# ===================
# VISTAS: EDITORIAL_PROVEEDOR (8 campos)
# ===================
def ver_editoriales(request):
    editoriales = EditorialProveedor.objects.all()
    return render(request, 'editorial_proveedor/ver_editoriales.html', {'editoriales': editoriales})

def agregar_editorial(request):
    if request.method == 'POST':
        EditorialProveedor.objects.create(
            nombre_oficial=request.POST.get('nombre_oficial'),
            nombre_comercial=request.POST.get('nombre_comercial'),
            pais=request.POST.get('pais'),
            contacto_nombre=request.POST.get('contacto_nombre'),
            contacto_email=request.POST.get('contacto_email'),
            telefono_internacional=request.POST.get('telefono_internacional'),
            direccion=request.POST.get('direccion')
        )
        return redirect('ver_editoriales')
    return render(request, 'editorial_proveedor/agregar_editorial.html')

def actualizar_editorial(request, id):
    editorial = get_object_or_404(EditorialProveedor, id=id)
    return render(request, 'editorial_proveedor/actualizar_editorial.html', {'editorial': editorial})

def realizar_actualizacion_editorial(request, id):
    editorial = get_object_or_404(EditorialProveedor, id=id)
    if request.method == 'POST':
        editorial.nombre_oficial = request.POST.get('nombre_oficial')
        editorial.nombre_comercial = request.POST.get('nombre_comercial')
        editorial.pais = request.POST.get('pais')
        editorial.contacto_nombre = request.POST.get('contacto_nombre')
        editorial.contacto_email = request.POST.get('contacto_email')
        editorial.telefono_internacional = request.POST.get('telefono_internacional')
        editorial.direccion = request.POST.get('direccion')
        editorial.save()
        return redirect('ver_editoriales')
    return render(request, 'editorial_proveedor/actualizar_editorial.html', {'editorial': editorial})

def borrar_editorial(request, id):
    editorial = get_object_or_404(EditorialProveedor, id=id)
    if request.method == 'POST':
        editorial.delete()
        return redirect('ver_editoriales')
    return render(request, 'editorial_proveedor/borrar_editorial.html', {'editorial': editorial})

# ===================
# VISTAS: PRODUCTOS_GLOBAL (7 campos)
# ===================
def ver_productos(request):
    productos = ProductosGlobal.objects.all()
    return render(request, 'productos_global/ver_productos.html', {'productos': productos})

def agregar_producto(request):
    editoriales = EditorialProveedor.objects.all()
    if request.method == 'POST':
        editorial_obj = None
        editorial_id = request.POST.get('editorial')
        if editorial_id:
            editorial_obj = get_object_or_404(EditorialProveedor, id=editorial_id)
            
        ProductosGlobal.objects.create(
            isbo=request.POST.get('isbo'),
            nombre=request.POST.get('nombre'),
            idioma=request.POST.get('idioma'),
            precio_base_usd=request.POST.get('precio_base_usd'),
            tipo_producto=request.POST.get('tipo_producto'),
            editorial=editorial_obj
        )
        return redirect('ver_productos')
    return render(request, 'productos_global/agregar_producto.html', {'editoriales': editoriales})

def actualizar_producto(request, id):
    producto = get_object_or_404(ProductosGlobal, id=id)
    editoriales = EditorialProveedor.objects.all()
    context = {'producto': producto, 'editoriales': editoriales}
    return render(request, 'productos_global/actualizar_producto.html', context)

def realizar_actualizacion_producto(request, id):
    producto = get_object_or_404(ProductosGlobal, id=id)
    if request.method == 'POST':
        editorial_obj = None
        editorial_id = request.POST.get('editorial')
        if editorial_id:
            editorial_obj = get_object_or_404(EditorialProveedor, id=editorial_id)

        producto.isbo = request.POST.get('isbo')
        producto.nombre = request.POST.get('nombre')
        producto.idioma = request.POST.get('idioma')
        producto.precio_base_usd = request.POST.get('precio_base_usd')
        producto.tipo_producto = request.POST.get('tipo_producto')
        producto.editorial = editorial_obj
        producto.save()
        return redirect('ver_productos')
    editoriales = EditorialProveedor.objects.all()
    context = {'producto': producto, 'editoriales': editoriales}
    return render(request, 'productos_global/actualizar_producto.html', context)

def borrar_producto(request, id):
    producto = get_object_or_404(ProductosGlobal, id=id)
    if request.method == 'POST':
        producto.delete()
        return redirect('ver_productos')
    return render(request, 'productos_global/borrar_producto.html', {'producto': producto})

# ===================
# VISTAS: INVENTARIO (9 campos)
# ===================
def ver_inventarios(request):
    inventarios = Inventario.objects.all()
    return render(request, 'inventario/ver_inventarios.html', {'inventarios': inventarios})

def agregar_inventario(request):
    productos = ProductosGlobal.objects.filter(inventario__isnull=True) 
    if request.method == 'POST':
        producto_obj = get_object_or_404(ProductosGlobal, id=request.POST.get('producto'))
        Inventario.objects.create(
            producto=producto_obj,
            almacen_ubicacion=request.POST.get('almacen_ubicacion'),
            cantidad_disponible=request.POST.get('cantidad_disponible', 0),
            costo_unitario=request.POST.get('costo_unitario', 0),
            minimo_stock=request.POST.get('minimo_stock', 0),
            maximo_stock=request.POST.get('maximo_stock', 100),
            fecha_recepcion=request.POST.get('fecha_recepcion') or None
        )
        return redirect('ver_inventarios')
    return render(request, 'inventario/agregar_inventario.html', {'productos': productos})

def actualizar_inventario(request, id):
    inventario = get_object_or_404(Inventario, id=id)
    return render(request, 'inventario/actualizar_inventario.html', {'inventario': inventario})

def realizar_actualizacion_inventario(request, id):
    inventario = get_object_or_404(Inventario, id=id)
    if request.method == 'POST':
        inventario.almacen_ubicacion = request.POST.get('almacen_ubicacion')
        inventario.cantidad_disponible = request.POST.get('cantidad_disponible')
        inventario.costo_unitario = request.POST.get('costo_unitario')
        inventario.minimo_stock = request.POST.get('minimo_stock')
        inventario.maximo_stock = request.POST.get('maximo_stock')
        inventario.fecha_recepcion = request.POST.get('fecha_recepcion') or None
        inventario.save()
        return redirect('ver_inventarios')
    return render(request, 'inventario/actualizar_inventario.html', {'inventario': inventario})

def borrar_inventario(request, id):
    inventario = get_object_or_404(Inventario, id=id)
    if request.method == 'POST':
        inventario.delete()
        return redirect('ver_inventarios')
    return render(request, 'inventario/borrar_inventario.html', {'inventario': inventario})

# ===================
# VISTAS: DETALLE_PEDIDO (¡CORREGIDAS CON 10 CAMPOS!)
# ===================
def ver_detalles(request):
    detalles = DetallePedido.objects.all().order_by('pedido', 'numero_linea')
    return render(request, 'detalle_pedido/ver_detalles.html', {'detalles': detalles})

def agregar_detalle_pedido(request):
    pedidos = Pedido.objects.all() 
    productos = ProductosGlobal.objects.all() 
    if request.method == 'POST':
        pedido_obj = get_object_or_404(Pedido, id=request.POST.get('pedido'))
        producto_obj = get_object_or_404(ProductosGlobal, id=request.POST.get('producto')) 
        
        DetallePedido.objects.create(
            pedido=pedido_obj,
            producto=producto_obj, 
            cantidad=request.POST.get('cantidad', 1),
            precio_venta_unitario=request.POST.get('precio_venta_unitario', 0),
            subtotal_detalle=request.POST.get('subtotal_detalle', 0),
            porcentaje_descuento=request.POST.get('porcentaje_descuento', 0),
            impuesto_detalle=request.POST.get('impuesto_detalle', 0),
            notas_item=request.POST.get('notas_item'),
            numero_linea=request.POST.get('numero_linea')
        )
        return redirect('ver_detalles')
    
    context = {'pedidos': pedidos, 'productos': productos}
    return render(request, 'detalle_pedido/agregar_detalle_pedido.html', context)

def actualizar_detalle_pedido(request, id):
    detalle = get_object_or_404(DetallePedido, id=id)
    pedidos = Pedido.objects.all()
    productos = ProductosGlobal.objects.all() 
    context = {'detalle': detalle, 'pedidos': pedidos, 'productos': productos}
    return render(request, 'detalle_pedido/actualizar_detalle_pedido.html', context)

def realizar_actualizacion_detalle_pedido(request, id):
    detalle = get_object_or_404(DetallePedido, id=id)
    if request.method == 'POST':
        detalle.pedido = get_object_or_404(Pedido, id=request.POST.get('pedido'))
        detalle.producto = get_object_or_404(ProductosGlobal, id=request.POST.get('producto')) 
        detalle.cantidad = request.POST.get('cantidad')
        detalle.precio_venta_unitario = request.POST.get('precio_venta_unitario')
        detalle.subtotal_detalle=request.POST.get('subtotal_detalle')
        detalle.porcentaje_descuento=request.POST.get('porcentaje_descuento')
        detalle.impuesto_detalle=request.POST.get('impuesto_detalle')
        detalle.notas_item=request.POST.get('notas_item')
        detalle.numero_linea=request.POST.get('numero_linea')
        detalle.save()
        return redirect('ver_detalles')
    
    pedidos = Pedido.objects.all()
    productos = ProductosGlobal.objects.all() 
    context = {'detalle': detalle, 'pedidos': pedidos, 'productos': productos}
    return render(request, 'detalle_pedido/actualizar_detalle_pedido.html', context)

def borrar_detalle_pedido(request, id):
    detalle = get_object_or_404(DetallePedido, id=id)
    if request.method == 'POST':
        detalle.delete()
        return redirect('ver_detalles')
    return render(request, 'detalle_pedido/borrar_detalle_pedido.html', {'detalle': detalle})