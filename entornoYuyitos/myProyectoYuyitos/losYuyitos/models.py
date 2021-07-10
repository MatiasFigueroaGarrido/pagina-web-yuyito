# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128, blank=True, null=True)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150, blank=True, null=True)
    first_name = models.CharField(max_length=150, blank=True, null=True)
    last_name = models.CharField(max_length=150, blank=True, null=True)
    email = models.CharField(max_length=254, blank=True, null=True)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Boleta(models.Model):
    nro_boleta = models.IntegerField(primary_key=True)
    fecha_venta = models.DateField()
    total_venta = models.IntegerField()
    total_descuentos = models.IntegerField()
    monto_total = models.IntegerField()
    monto_pago = models.IntegerField()
    trabajador_rut_trab = models.ForeignKey('Trabajador', models.DO_NOTHING, db_column='trabajador_rut_trab')
    tipo_venta_id_tipventa = models.ForeignKey('TipoVenta', models.DO_NOTHING, db_column='tipo_venta_id_tipventa')
    fecha_entrega = models.DateField(blank=True, null=True)
    nom_cliente = models.CharField(max_length=40, blank=True, null=True)
    direccion_cliente = models.CharField(max_length=50, blank=True, null=True)
    fono_contacto = models.BigIntegerField(blank=True, null=True)
    estado_ped_id_estadelivery = models.ForeignKey('EstadoPed', models.DO_NOTHING, db_column='estado_ped_id_estadelivery', blank=True, null=True)
    cliente_rut_cli = models.ForeignKey('Cliente', models.DO_NOTHING, db_column='cliente_rut_cli', blank=True, null=True)
    estado_deuda_id_estadeuda = models.ForeignKey('EstadoDeuda', models.DO_NOTHING, db_column='estado_deuda_id_estadeuda', blank=True, null=True)
    medio_pago_id_mediopago = models.ForeignKey('MedioPago', models.DO_NOTHING, db_column='medio_pago_id_mediopago')

    class Meta:
        managed = False
        db_table = 'boleta'


class CargoTrabajador(models.Model):
    id_cargo = models.FloatField(primary_key=True)
    nombre_cargo = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'cargo_trabajador'


class Cliente(models.Model):
    rut_cli = models.CharField(primary_key=True, max_length=9)
    nombre_cli = models.CharField(max_length=50)
    apellido_cli = models.CharField(max_length=50)
    fono_cli = models.IntegerField()
    correo_cli = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'cliente'


class ControlRecep(models.Model):
    id_recepcion = models.IntegerField(primary_key=True)
    valor_pagado_recep = models.IntegerField()
    fech_recepcion = models.DateField()
    orden_ped_id_orden = models.ForeignKey('OrdenPed', models.DO_NOTHING, db_column='orden_ped_id_orden')

    class Meta:
        managed = False
        db_table = 'control_recep'


class DetRecep(models.Model):
    cantidad_product = models.FloatField()
    control_recep_id_recepcion = models.ForeignKey(ControlRecep, models.DO_NOTHING, db_column='control_recep_id_recepcion')
    producto_codigo_producto = models.ForeignKey('Producto', models.DO_NOTHING, db_column='producto_codigo_producto')
    nom_product = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'det_recep'


class DetalleBoleta(models.Model):
    boleta_nro_boleta = models.ForeignKey(Boleta, models.DO_NOTHING, db_column='boleta_nro_boleta')
    producto_codigo_producto = models.ForeignKey('Producto', models.DO_NOTHING, db_column='producto_codigo_producto')
    canti_producto = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'detalle_boleta'


class DetalleOrden(models.Model):
    canti_product = models.IntegerField()
    orden_ped_id_orden = models.ForeignKey('OrdenPed', models.DO_NOTHING, db_column='orden_ped_id_orden')
    producto_codigo_producto = models.ForeignKey('Producto', models.DO_NOTHING, db_column='producto_codigo_producto')
    nom_product = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'detalle_orden'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200, blank=True, null=True)
    action_flag = models.IntegerField()
    change_message = models.TextField(blank=True, null=True)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100, blank=True, null=True)
    model = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField(blank=True, null=True)
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class EstadoCivil(models.Model):
    id_estac = models.FloatField(primary_key=True)
    descrip_estac = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'estado_civil'


class EstadoDeuda(models.Model):
    id_estadeuda = models.IntegerField(primary_key=True)
    descripcion_estadeuda = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'estado_deuda'


class EstadoPed(models.Model):
    id_estadelivery = models.IntegerField(primary_key=True)
    descrip_estadelivery = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'estado_ped'


class MedioPago(models.Model):
    id_mediopago = models.IntegerField(primary_key=True)
    descrip_mediopago = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'medio_pago'


class OrdenPed(models.Model):
    id_orden = models.IntegerField(primary_key=True)
    fech_orden = models.DateField()
    monto_orden = models.FloatField()
    proveedor_rut_provee = models.ForeignKey('Proveedor', models.DO_NOTHING, db_column='proveedor_rut_provee')
    descrip_orden = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'orden_ped'


class Pago(models.Model):
    id_pago = models.IntegerField(primary_key=True)
    fech_pago = models.DateField()
    monto_pago = models.IntegerField()
    medio_pago_id_mediopago = models.ForeignKey(MedioPago, models.DO_NOTHING, db_column='medio_pago_id_mediopago')
    boleta_nro_boleta = models.ForeignKey(Boleta, models.DO_NOTHING, db_column='boleta_nro_boleta')

    class Meta:
        managed = False
        db_table = 'pago'


class Producto(models.Model):
    codigo_producto = models.BigIntegerField(primary_key=True)
    nombre_product = models.CharField(max_length=50)
    precio_compra = models.IntegerField()
    precio_venta = models.IntegerField()
    stock = models.FloatField()
    stock_critico = models.FloatField()
    fech_elabo_product = models.DateField()
    fech_venci_product = models.DateField()
    marca = models.CharField(max_length=100)
    cod_barra_product = models.BigIntegerField()
    img_produc = models.BinaryField()
    tipo_producto_id_tipproduc = models.ForeignKey('TipoProducto', models.DO_NOTHING, db_column='tipo_producto_id_tipproduc')
    proveedor_rut_provee = models.ForeignKey('Proveedor', models.DO_NOTHING, db_column='proveedor_rut_provee', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'producto'


class Promocion(models.Model):
    id_promocion = models.IntegerField(primary_key=True)
    imagen_promo = models.BinaryField()
    fecha_inicio_promo = models.DateField()
    fecha_fin_promo = models.DateField()
    descrip_promo = models.CharField(max_length=100)
    cant_producto = models.IntegerField(blank=True, null=True)
    descuento_porcentaje = models.IntegerField()
    descuento_efectivo = models.IntegerField()
    tipo_producto_id_tipproduc = models.ForeignKey('TipoProducto', models.DO_NOTHING, db_column='tipo_producto_id_tipproduc', blank=True, null=True)
    tipo_promocion_id_tipopromo = models.ForeignKey('TipoPromocion', models.DO_NOTHING, db_column='tipo_promocion_id_tipopromo')

    class Meta:
        managed = False
        db_table = 'promocion'


class Proveedor(models.Model):
    rut_provee = models.CharField(primary_key=True, max_length=9)
    nombre_provee = models.CharField(max_length=50)
    direccion_provee = models.CharField(max_length=100)
    telefono_1_provee = models.IntegerField()
    telefono_2_provee = models.IntegerField(blank=True, null=True)
    nom_servidor = models.CharField(max_length=50)
    telefono_servidor = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'proveedor'


class TipoProducto(models.Model):
    id_tipproduc = models.IntegerField(primary_key=True)
    descrip_tipproduc = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'tipo_producto'


class TipoPromocion(models.Model):
    id_tipopromo = models.IntegerField(primary_key=True)
    descrip_tipopromo = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'tipo_promocion'


class TipoVenta(models.Model):
    id_tipventa = models.IntegerField(primary_key=True)
    descrip_tipventa = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'tipo_venta'


class Trabajador(models.Model):
    rut_trab = models.CharField(primary_key=True, max_length=9)
    nombre_trab = models.CharField(max_length=50)
    apellido_trab = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    correo = models.CharField(unique=True, max_length=100)
    nom_usuario = models.CharField(unique=True, max_length=40)
    contrasena_usuario = models.CharField(max_length=50)
    cargo_trabajador_id_cargo = models.ForeignKey(CargoTrabajador, models.DO_NOTHING, db_column='cargo_trabajador_id_cargo')
    estado_civil_id_estac = models.ForeignKey(EstadoCivil, models.DO_NOTHING, db_column='estado_civil_id_estac')

    class Meta:
        managed = False
        db_table = 'trabajador'
