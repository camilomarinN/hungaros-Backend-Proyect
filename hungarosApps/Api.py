from .base_viewset import BaseModelViewSet
from rest_framework import permissions, status
from .models import (
    Usuarios, Roles, Permisos, PermisosPorRoles, TipoProductos,
    Productos, Fiados, ProductosPorFiados, Auditorias
)
from .serializers import (
    UsuariosSerializer, RolesSerializer, PermisosSerializer, PermisosPorRolesSerializer,
    TipoProductosSerializer, ProductosSerializer, FiadosSerializer, ProductosPorFiadosSerializer,
    AuditoriasSerializer
)

class UsuariosViewSet(BaseModelViewSet):
    queryset = Usuarios.objects.all()
    serializer_class = UsuariosSerializer
    permission_classes = [permissions.IsAuthenticated]

class RolesViewSet(BaseModelViewSet):
    queryset = Roles.objects.all()
    serializer_class = RolesSerializer
    permission_classes = [permissions.IsAuthenticated]

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

class ProductosViewSet(BaseModelViewSet):
    queryset = Productos.objects.all()
    serializer_class = ProductosSerializer
    permission_classes = [permissions.IsAuthenticated]

class FiadosViewSet(BaseModelViewSet):
    queryset = Fiados.objects.all()
    serializer_class = FiadosSerializer
    permission_classes = [permissions.IsAuthenticated]

class ProductosPorFiadosViewSet(BaseModelViewSet):
    queryset = ProductosPorFiados.objects.all()
    serializer_class = ProductosPorFiadosSerializer
    permission_classes = [permissions.IsAuthenticated]

class AuditoriasViewSet(BaseModelViewSet):
    queryset = Auditorias.objects.all()
    serializer_class = AuditoriasSerializer
    permission_classes = [permissions.IsAuthenticated]
