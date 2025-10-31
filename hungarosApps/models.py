from django.db import models


class Auditorias(models.Model):
    id_auditoria = models.BigIntegerField(primary_key=True)
    id_usuario = models.ForeignKey('Usuarios', models.DO_NOTHING, db_column='id_usuario', blank=False, null=False)
    fecha_auditoria = models.DateField(blank=False, null=False)
    accion_auditoria = models.CharField(max_length=20, blank=False, null=False)
    tabla_auditoria = models.CharField(max_length=20, blank=False, null=False)
    descripcion_auditoria = models.CharField(max_length=100, blank=False, null=False)

    class Meta:
        managed = False
        db_table = 'auditorias'


class Fiados(models.Model):
    id_fiado = models.BigIntegerField(primary_key=True)
    id_usuario_fiado = models.ForeignKey('Usuarios', models.DO_NOTHING, db_column='id_usuario_fiado', blank=False, null=False)
    fecha_fiado = models.DateField(blank=False, null=False)
    valor_fiado = models.IntegerField(blank=False, null=False)
    descripcion_fiado = models.CharField(max_length=50, blank=False, null=False)

    class Meta:
        managed = False
        db_table = 'fiados'


class Permisos(models.Model):
    id_permiso = models.BigIntegerField(primary_key=True)
    nombre_permiso = models.CharField(unique=True, max_length=20, blank=False, null=False)

    class Meta:
        managed = False
        db_table = 'permisos'


class PermisosPorRoles(models.Model):
    pk = models.CompositePrimaryKey('id_rol', 'id_permiso')
    id_rol = models.ForeignKey('Roles', models.DO_NOTHING, db_column='id_rol')
    id_permiso = models.ForeignKey(Permisos, models.DO_NOTHING, db_column='id_permiso')

    class Meta:
        managed = False
        db_table = 'permisosporroles'


class Productos(models.Model):
    id_producto = models.BigIntegerField(primary_key=True)
    nombre_producto = models.CharField(unique=True, max_length=50, blank=False, null=False)
    precio_producto = models.IntegerField(blank=False, null=False)
    id_tipo_producto = models.ForeignKey('Tipoproductos', models.DO_NOTHING, db_column='id_tipo_producto', blank=False, null=False)

    class Meta:
        managed = False
        db_table = 'productos'


class ProductosPorFiados(models.Model):
    pk = models.CompositePrimaryKey('id_fiado', 'id_producto')
    id_fiado = models.ForeignKey(Fiados, models.DO_NOTHING, db_column='id_fiado')
    id_producto = models.ForeignKey(Productos, models.DO_NOTHING, db_column='id_producto')

    class Meta:
        managed = False
        db_table = 'productosporfiados'


class Roles(models.Model):
    id_rol = models.BigIntegerField(primary_key=True)
    nombre_rol = models.CharField(unique=True, max_length=20, blank=False, null=False)

    class Meta:
        managed = False
        db_table = 'roles'


class TipoProductos(models.Model):
    id_tipo_producto = models.IntegerField(primary_key=True)
    nombre_tipo_producto = models.CharField(unique=True, max_length=50, blank=False, null=False)

    class Meta:
        managed = False
        db_table = 'tipoproductos'


class Usuarios(models.Model):
    id_usuario = models.CharField(primary_key=True, max_length=20)
    nombre_usu = models.CharField(max_length=50, blank=False, null=False)
    primer_apellido_usu = models.CharField(max_length=50, blank=False, null=False)
    segundo_apellido_usu = models.CharField(max_length=50, blank=True, null=True)
    hash_contrasena_usu = models.CharField(max_length=255, blank=False, null=False)
    fecha_ingreso_usu = models.DateField(blank=False, null=False)
    id_rol = models.ForeignKey(Roles, models.DO_NOTHING, db_column='id_rol', blank=False, null=False)

    class Meta:
        managed = False
        db_table = 'usuarios'
