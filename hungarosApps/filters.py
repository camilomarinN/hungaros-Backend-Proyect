import django_filters
from django.db.models import Q
from .models import Fiados, Productos, Usuarios, Auditorias, ProductosPorFiados, Roles, TipoProductos


class FiadosFilter(django_filters.FilterSet):
    cliente = django_filters.CharFilter(field_name="id_usuario_fiado__id_usuario", lookup_expr="iexact")
    nombre_cliente = django_filters.CharFilter(field_name="id_usuario_fiado__nombre_usu", lookup_expr="icontains")
    apellido_cliente = django_filters.CharFilter(field_name="id_usuario_fiado__primer_apellido_usu", lookup_expr="icontains")
    fecha_desde = django_filters.DateFilter(field_name="fecha_fiado", lookup_expr="gte")
    fecha_hasta = django_filters.DateFilter(field_name="fecha_fiado", lookup_expr="lte")
    valor_min = django_filters.NumberFilter(field_name="valor_fiado", lookup_expr="gte")
    valor_max = django_filters.NumberFilter(field_name="valor_fiado", lookup_expr="lte")

    class Meta:
        model = Fiados
        fields = ["cliente", "nombre_cliente", "apellido_cliente", "fecha_desde", "fecha_hasta", "valor_min", "valor_max"]


class ProductosFilter(django_filters.FilterSet):
    nombre = django_filters.CharFilter(field_name="nombre_producto", lookup_expr="icontains")
    tipo = django_filters.NumberFilter(field_name="id_tipo_producto")
    precio_min = django_filters.NumberFilter(field_name="precio_producto", lookup_expr="gte")
    precio_max = django_filters.NumberFilter(field_name="precio_producto", lookup_expr="lte")

    class Meta:
        model = Productos
        fields = ["nombre", "tipo", "precio_min", "precio_max"]


class TipoProductosFilter(django_filters.FilterSet):
    nombre = django_filters.CharFilter(field_name="nombre_tipo_producto", lookup_expr="icontains")

    class Meta:
        model = TipoProductos
        fields = ["nombre"]


class UsuariosFilter(django_filters.FilterSet):
    nombre = django_filters.CharFilter(field_name="nombre_usu", lookup_expr="icontains")
    apellido = django_filters.CharFilter(field_name="primer_apellido_usu", lookup_expr="icontains")
    rol = django_filters.NumberFilter(field_name="id_rol")
    fecha_ingreso_desde = django_filters.DateFilter(field_name="fecha_ingreso_usu", lookup_expr="gte")
    fecha_ingreso_hasta = django_filters.DateFilter(field_name="fecha_ingreso_usu", lookup_expr="lte")
    busqueda = django_filters.CharFilter(method="filter_busqueda")

    class Meta:
        model = Usuarios
        fields = ["nombre", "apellido", "rol", "fecha_ingreso_desde", "fecha_ingreso_hasta", "busqueda"]

    def filter_busqueda(self, queryset, name, value):
        terminos = value.split()
        query = Q()
        for termino in terminos:
            query &= (
                Q(nombre_usu__icontains=termino)
                | Q(primer_apellido_usu__icontains=termino)
                | Q(segundo_apellido_usu__icontains=termino)
                | Q(id_usuario__icontains=termino)
            )
        return queryset.filter(query)


class AuditoriasFilter(django_filters.FilterSet):
    usuario = django_filters.CharFilter(field_name="id_usuario", lookup_expr="iexact")
    accion = django_filters.CharFilter(field_name="accion_auditoria", lookup_expr="icontains")
    tabla = django_filters.CharFilter(field_name="tabla_auditoria", lookup_expr="icontains")
    fecha_desde = django_filters.DateFilter(field_name="fecha_auditoria", lookup_expr="gte")
    fecha_hasta = django_filters.DateFilter(field_name="fecha_auditoria", lookup_expr="lte")

    class Meta:
        model = Auditorias
        fields = ["usuario", "accion", "tabla", "fecha_desde", "fecha_hasta"]


class ProductosPorFiadosFilter(django_filters.FilterSet):
    fiado = django_filters.NumberFilter(field_name="id_fiado")
    producto = django_filters.NumberFilter(field_name="id_producto")

    class Meta:
        model = ProductosPorFiados
        fields = ["fiado", "producto"]


class RolesFilter(django_filters.FilterSet):
    nombre_rol = django_filters.CharFilter(field_name="nombre_rol", lookup_expr="icontains")

    class Meta:
        model = Roles
        fields = ["nombre_rol"]