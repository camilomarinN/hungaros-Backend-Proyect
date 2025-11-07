from rest_framework import serializers
from .security_utils import hash_password
from .models import (Usuarios, Roles, Permisos, PermisosPorRoles, TipoProductos, Productos, Fiados, ProductosPorFiados, Auditorias)

class UsuariosSerializer(serializers.ModelSerializer):
    hash_contrasena_usu = serializers.CharField(write_only=True)
    class Meta:
        model = Usuarios
        fields = [
            'id_usuario',
            'nombre_usu',
            'primer_apellido_usu',
            'segundo_apellido_usu',
            'hash_contrasena_usu',
            'fecha_ingreso_usu',
            'id_rol'
        ]
        read_only_fields = ['fecha_ingreso_usu']
    def create(self, validated_data):
        plain_password = validated_data.pop('hash_contrasena_usu')
        if not plain_password:
            raise serializers.ValidationError("La contraseña no puede estar vacía.")
        validated_data['hash_contrasena_usu'] = hash_password(plain_password)
        return super().create(validated_data)


    def update(self, instance, validated_data):
        if 'hash_contrasena_usu' in validated_data:
            plain_password = validated_data.pop('hash_contrasena_usu')
            validated_data['hash_contrasena_usu'] = hash_password(plain_password)
        return super().update(instance, validated_data)

class RolesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Roles
        fields = ['id_rol', 'nombre_rol']
        read_only_fields = ['id_rol']

class PermisosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permisos
        fields = ['id_permiso', 'nombre_permiso']
        read_only_fields = ['id_permiso']

class PermisosPorRolesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PermisosPorRoles
        fields = ['id_rol', 'id_permiso']
        read_only_fields = []

class TipoProductosSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoProductos
        fields = ['id_tipo_producto', 'nombre_tipo_producto']
        read_only_fields = ['id_tipo_producto']

class ProductosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Productos
        fields = ['id_producto', 'nombre_producto', 'precio_producto', 'id_tipo_producto']
        read_only_fields = ['id_producto']

class FiadosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fiados
        fields = ['id_fiado', 'id_usuario_fiado', 'fecha_fiado', 'valor_fiado', 'descripcion_fiado']
        read_only_fields = ['id_fiado']

class ProductosPorFiadosSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductosPorFiados
        fields = ['id_fiado', 'id_producto']
        read_only_fields = []

class AuditoriasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Auditorias
        fields = [
            'id_auditoria',
            'id_usuario',
            'fecha_auditoria',
            'accion_auditoria',
            'tabla_auditoria',
            'descripcion_auditoria'
        ]
        read_only_fields = ['id_auditoria', 'fecha_auditoria']
