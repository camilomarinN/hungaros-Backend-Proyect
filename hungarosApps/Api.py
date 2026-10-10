from .base_viewset import BaseModelViewSet
from rest_framework import permissions
from django.db import transaction
from .models import (
    Usuarios, Roles, Permisos, PermisosPorRoles, TipoProductos,
    Productos, Fiados, ProductosPorFiados, Auditorias
)
from .serializers import (
    UsuariosSerializer, RolesSerializer, PermisosSerializer, PermisosPorRolesSerializer,
    TipoProductosSerializer, ProductosSerializer, FiadosSerializer,
    ProductosPorFiadosSerializer, AuditoriasSerializer
)

from .filters import (
    FiadosFilter, ProductosFilter, UsuariosFilter,
    AuditoriasFilter, ProductosPorFiadosFilter, RolesFilter, TipoProductosFilter
)


class UsuariosViewSet(BaseModelViewSet):
    queryset = Usuarios.objects.all()
    serializer_class = UsuariosSerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_class = UsuariosFilter


class RolesViewSet(BaseModelViewSet):
    queryset = Roles.objects.all()
    serializer_class = RolesSerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_class = RolesFilter


class PermisosViewSet(BaseModelViewSet):
    queryset = Permisos.objects.all()
    serializer_class = PermisosSerializer
    permission_classes = [permissions.IsAuthenticated]


class PermisosPorRolesViewSet(BaseModelViewSet):
    queryset = PermisosPorRoles.objects.all()
    serializer_class = PermisosPorRolesSerializer
    permission_classes = [permissions.IsAuthenticated]


class TipoProductosViewSet(BaseModelViewSet):
    queryset = TipoProductos.objects.all()
    serializer_class = TipoProductosSerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_class = TipoProductosFilter


class ProductosViewSet(BaseModelViewSet):
    queryset = Productos.objects.all()
    serializer_class = ProductosSerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_class = ProductosFilter


class FiadosViewSet(BaseModelViewSet):
    queryset = Fiados.objects.select_related("id_usuario_fiado").all()
    serializer_class = FiadosSerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_class = FiadosFilter

    def perform_destroy(self, instance):
        with transaction.atomic():
            ProductosPorFiados.objects.filter(id_fiado=instance.id_fiado).delete()
            instance.delete()


class ProductosPorFiadosViewSet(BaseModelViewSet):
    queryset = ProductosPorFiados.objects.all()
    serializer_class = ProductosPorFiadosSerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_class = ProductosPorFiadosFilter


class AuditoriasViewSet(BaseModelViewSet):
    queryset = Auditorias.objects.all()
    serializer_class = AuditoriasSerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_class = AuditoriasFilter