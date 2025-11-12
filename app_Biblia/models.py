from django.db import models

# ===================
# TABLA 1: CLIENTES GLOBAL (8 campos)
# ===================
class ClienteGlobal(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.CharField(max_length=255, unique=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    pais_residencia = models.CharField(max_length=100)
    codigo_postal = models.CharField(max_length=15, null=True, blank=True)
    telefono = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

# ===================
# TABLA 2: PEDIDOS (9 campos)
# ===================
class Pedido(models.Model):
    fecha_hora = models.DateTimeField(auto_now_add=True)
    total_neto = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    metodo_pago = models.CharField(max_length=50)
    estado_pedido = models.CharField(max_length=50, default='Pendiente')
    impuesto_total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    costo_envio = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    direccion_envio = models.CharField(max_length=255)

    cliente = models.ForeignKey(
        ClienteGlobal,
        on_delete=models.CASCADE,
        related_name="pedidos"
    )

    def __str__(self):
        return f"Pedido #{self.pk} - Cliente: {self.cliente.apellido}"

# ===================
# TABLA 3: EDITORIAL_PROVEEDOR (8 campos)
# ===================
class EditorialProveedor(models.Model):
    nombre_oficial = models.CharField(max_length=255)
    nombre_comercial = models.CharField(max_length=255, blank=True, null=True)
    pais = models.CharField(max_length=100, blank=True, null=True)
    contacto_nombre = models.CharField(max_length=100, blank=True, null=True)
    contacto_email = models.EmailField(max_length=254, blank=True, null=True)
    telefono_internacional = models.CharField(max_length=30, blank=True, null=True)
    direccion = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "Editoriales y Proveedores"
        ordering = ['nombre_oficial']

    def __str__(self):
        return self.nombre_oficial

# ===================
# TABLA 4: PRODUCTOS_GLOBAL (7 campos)
# ===================
class ProductosGlobal(models.Model):
    isbo = models.CharField(max_length=20, unique=True) 
    nombre = models.CharField(max_length=255)
    idioma = models.CharField(max_length=50)
    precio_base_usd = models.DecimalField(max_digits=10, decimal_places=2)
    tipo_producto = models.CharField(max_length=100) 

    editorial = models.ForeignKey(
        EditorialProveedor,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="productos"
    )

    class Meta:
        verbose_name_plural = "Productos Globales"
        ordering = ['nombre']

    def __str__(self):
        return self.nombre

# ===================
# TABLA 5: INVENTARIO (9 campos)
# ===================
class Inventario(models.Model):
    almacen_ubicacion = models.CharField(max_length=255)
    cantidad_disponible = models.PositiveIntegerField(default=0)
    costo_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    ultima_actualizacion = models.DateTimeField(auto_now=True)
    minimo_stock = models.PositiveIntegerField(default=0)
    maximo_stock = models.PositiveIntegerField(default=100)
    fecha_recepcion = models.DateField(null=True, blank=True)

    producto = models.OneToOneField(
        ProductosGlobal,
        on_delete=models.CASCADE,
        related_name="inventario"
    )

    class Meta:
        verbose_name_plural = "Inventarios"

    def __str__(self):
        return f"Inventario de: {self.producto.nombre}"

# ===================
# TABLA 6: DETALLE_PEDIDO (¡CORREGIDA CON 10 CAMPOS!)
# ===================
class DetallePedido(models.Model):
    cantidad = models.PositiveIntegerField(default=1)
    precio_venta_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    # --- ¡ESTOS SON LOS CAMPOS QUE FALTABAN EN TU ARCHIVO! ---
    subtotal_detalle = models.DecimalField(max_digits=10, decimal_places=2)
    porcentaje_descuento = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    impuesto_detalle = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    notas_item = models.CharField(max_length=255, blank=True, null=True)
    numero_linea = models.PositiveIntegerField()

    pedido = models.ForeignKey(
        Pedido,
        on_delete=models.CASCADE,
        related_name="detalles"
    )

    producto = models.ForeignKey(
        ProductosGlobal,
        on_delete=models.SET_NULL,
        null=True
    )

    class Meta:
        verbose_name_plural = "Detalles de Pedido"
        ordering = ['pedido', 'numero_linea']

    def __str__(self):
        return f"Detalle de Pedido #{self.pedido.pk}, Línea {self.numero_linea}"