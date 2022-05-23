#from django.db import models

# Create your models here.
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Bodega(models.Model):
    id_bodega = models.AutoField(primary_key=True)
    codigo_bodega = models.CharField(max_length=255)
    nombre_bodega = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'bodega'


class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    id_estado_cliente = models.ForeignKey('EstadoCliente', models.DO_NOTHING, db_column='id_estado_cliente')
    id_comuna = models.ForeignKey('Comuna', models.DO_NOTHING, db_column='id_comuna')
    id_forma_pago = models.ForeignKey('FormaPago', models.DO_NOTHING, db_column='id_forma_pago')
    rut_cliente = models.CharField(max_length=255)
    razon_social_cliente = models.CharField(max_length=255)
    nombre_fantasia_cliente = models.CharField(max_length=255)
    direccion_comercial_cliente = models.CharField(max_length=255)
    direccion_logistica_cliente = models.CharField(max_length=255)
    holding_cliente = models.CharField(max_length=255)
    email_sii_cliente = models.CharField(max_length=255)
    fecha_registro_cliente = models.DateField()
    fecha_modificacion_cliente = models.DateField()

    class Meta:
        managed = False
        db_table = 'cliente'


class Comuna(models.Model):
    id_comuna = models.AutoField(primary_key=True)
    nombre_comuna = models.CharField(max_length=255)
    provincia_comuna = models.CharField(max_length=255)
    region_comuna = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'comuna'


class Contacto(models.Model):
    id_contacto = models.AutoField(primary_key=True)
    id_cliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='id_cliente')
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    fono = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    cargo = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'contacto'


class DetalleDocProducto(models.Model):
    id_detalle_documento = models.ForeignKey('DetalleDocumento', models.DO_NOTHING, db_column='id_detalle_documento')
    id_producto = models.ForeignKey('Producto', models.DO_NOTHING, db_column='id_producto')
    cantidad = models.IntegerField()
    valor_unitario = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'detalle_doc_producto'


class DetalleDocumento(models.Model):
    id_detalle_documento = models.AutoField(primary_key=True)
    id_encabezado_documento = models.ForeignKey('EncabezadoDocumento', models.DO_NOTHING, db_column='id_encabezado_documento')
    id_estado_item = models.ForeignKey('EstadoItem', models.DO_NOTHING, db_column='id_estado_item', blank=True, null=True)
    total_item = models.IntegerField()
    descuento_item = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'detalle_documento'


class DocuRefTipoDocRef(models.Model):
    id_documento_referencia = models.ForeignKey('DocumentoReferencia', models.DO_NOTHING, db_column='id_documento_referencia')
    id_tipo_documento_referencia = models.ForeignKey('TipoDocumentoReferencia', models.DO_NOTHING, db_column='id_tipo_documento_referencia')

    class Meta:
        managed = False
        db_table = 'docu_ref_tipo_doc_ref'


class DocumentoReferencia(models.Model):
    id_documento_referencia = models.AutoField(primary_key=True)
    numero_referencia = models.IntegerField(blank=True, null=True)
    numero_fecha = models.DateField()
    numero_factura = models.IntegerField(blank=True, null=True)
    motivo_anulacion = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'documento_referencia'


class EncabezadoDocumento(models.Model):
    id_encabezado_documento = models.AutoField(primary_key=True)
    id_cliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='id_cliente')
    id_tipo_contrato = models.ForeignKey('TipoContrato', models.DO_NOTHING, db_column='id_tipo_contrato', blank=True, null=True)
    id_documento_referencia = models.ForeignKey(DocumentoReferencia, models.DO_NOTHING, db_column='id_documento_referencia', blank=True, null=True)
    id_tipo_documento = models.ForeignKey('TipoDocumento', models.DO_NOTHING, db_column='id_tipo_documento', blank=True, null=True)
    id_tipo_cambio = models.ForeignKey('TipoCambio', models.DO_NOTHING, db_column='id_tipo_cambio')
    nro_documento = models.IntegerField()
    fecha_documento = models.DateField()
    fecha_vencimiento = models.DateField(blank=True, null=True)
    total_neto = models.IntegerField()
    iva = models.IntegerField()
    total_iva = models.IntegerField()
    total_descuento = models.IntegerField(blank=True, null=True)
    fecha_registro = models.DateField()
    fecha_modificacion = models.DateField(blank=True, null=True)
    estado_envio_publicado = models.IntegerField(blank=True, null=True)
    comentario_observacion = models.CharField(max_length=255, blank=True, null=True)
    num_ciclo = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'encabezado_documento'


class EstadoCliente(models.Model):
    id_estado_cliente = models.AutoField(primary_key=True)
    desc_estado = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'estado_cliente'


class EstadoDocEncabezado(models.Model):
    id_encabezado_documento = models.ForeignKey(EncabezadoDocumento, models.DO_NOTHING, db_column='id_encabezado_documento')
    id_estado_documento = models.ForeignKey('EstadoDocumento', models.DO_NOTHING, db_column='id_estado_documento')
    fecha_estado = models.DateField()

    class Meta:
        managed = False
        db_table = 'estado_doc_encabezado'


class EstadoDocumento(models.Model):
    id_estado_documento = models.AutoField(primary_key=True)
    codigo_estado_documento = models.IntegerField()
    nombre_estado_documento = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'estado_documento'


class EstadoItem(models.Model):
    id_estado_item = models.AutoField(primary_key=True)
    codigo_estado_item = models.IntegerField()
    nombre_estado_item = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'estado_item'


class FormaPago(models.Model):
    id_forma_pago = models.AutoField(primary_key=True)
    nombre_forma_pago = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'forma_pago'


class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True)
    id_unidad_medida = models.ForeignKey('UnidadMedida', models.DO_NOTHING, db_column='id_unidad_medida')
    id_stock = models.ForeignKey('Stock', models.DO_NOTHING, db_column='id_stock', blank=True, null=True)
    codigo_producto = models.IntegerField()
    nombre_producto = models.CharField(max_length=255)
    nombre_producto_proveedor = models.CharField(max_length=255)
    codigo_producto_proveedor = models.IntegerField()
    nombre_proveedor = models.CharField(max_length=255)
    estado_producto = models.CharField(max_length=255)
    codigo_barra_productos = models.IntegerField()
    fecha_registro = models.DateField()
    fecha_modificacion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'producto'


class ProductoReceta(models.Model):
    id_receta = models.ForeignKey('Receta', models.DO_NOTHING, db_column='id_receta')
    id_producto = models.ForeignKey(Producto, models.DO_NOTHING, db_column='id_producto')
    cantidad_producto = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'producto_receta'


class Receta(models.Model):
    id_receta = models.AutoField(primary_key=True)
    nombre_receta = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'receta'


class Stock(models.Model):
    id_stock = models.AutoField(primary_key=True)
    cantidad_stock = models.IntegerField()
    por_llegar_cantidad = models.IntegerField()
    por_llegar_fecha = models.DateField()
    numero_lote = models.IntegerField(blank=True, null=True)
    fecha_vencimiento_lote = models.DateField(blank=True, null=True)
    numero_serie_stock = models.IntegerField(blank=True, null=True)
    ubicacion_stock = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock'


class StockBodega(models.Model):
    id_bodega = models.ForeignKey(Bodega, models.DO_NOTHING, db_column='id_bodega')
    id_stock = models.ForeignKey(Stock, models.DO_NOTHING, db_column='id_stock')

    class Meta:
        managed = False
        db_table = 'stock_bodega'


class Sucursal(models.Model):
    id_sucursal = models.AutoField(primary_key=True)
    id_cliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='id_cliente')
    cod_sucursal = models.CharField(max_length=255)
    nombre_sucursal = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'sucursal'


class TipoCambio(models.Model):
    id_tipo_cambio = models.AutoField(primary_key=True)
    valor_tipo_cambio = models.IntegerField()
    nombre_tipo_cambio = models.CharField(max_length=1)
    cod_tipo_cambio = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipo_cambio'


class TipoContrato(models.Model):
    id_tipo_contrato = models.AutoField(primary_key=True)
    nombre_contrato = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'tipo_contrato'


class TipoDocumento(models.Model):
    id_tipo_documento = models.AutoField(primary_key=True)
    nombre_tipo_documento = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'tipo_documento'


class TipoDocumentoReferencia(models.Model):
    id_tipo_documento_referencia = models.AutoField(primary_key=True)
    codigo_documento_referencia = models.CharField(max_length=1)
    nombre_documento_referencia = models.CharField(max_length=1)
    devuelve_stock = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'tipo_documento_referencia'


class UnidadMedida(models.Model):
    id_unidad_medida = models.AutoField(primary_key=True)
    nombre_unidad = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'unidad_medida'

