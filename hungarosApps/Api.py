from rest_framework import viewsets, permissions
from .models import (
    Usuarios, Roles, Permisos, PermisosPorRoles, TipoProductos,
    Productos, Fiados, ProductosPorFiados, Auditorias
)
from .serializers import (
    UsuariosSerializer, RolesSerializer, PermisosSerializer, PermisosPorRolesSerializer,
    TipoProductosSerializer, ProductosSerializer, FiadosSerializer, ProductosPorFiadosSerializer,
    AuditoriasSerializer
)

class UsuariosViewSet(viewsets.ModelViewSet):
    queryset = Usuarios.objects.all()
    serializer_class = UsuariosSerializer
    permission_classes = [permissions.IsAuthenticated]

class RolesViewSet(viewsets.ModelViewSet):
    queryset = Roles.objects.all()
    serializer_class = RolesSerializer
    permission_classes = [permissions.IsAuthenticated]

class PermisosViewSet(viewsets.ModelViewSet):
    queryset = Permisos.objects.all()
    serializer_class = PermisosSerializer
    permission_classes = [permissions.IsAuthenticated]

class PermisosPorRolesViewSet(viewsets.ModelViewSet):
    queryset = PermisosPorRoles.objects.all()
    serializer_class = PermisosPorRolesSerializer
    permission_classes = [permissions.IsAuthenticated]

class TipoProductosViewSet(viewsets.ModelViewSet):
    queryset = TipoProductos.objects.all()
    serializer_class = TipoProductosSerializer
    permission_classes = [permissions.IsAuthenticated]

class ProductosViewSet(viewsets.ModelViewSet):
    queryset = Productos.objects.all()
    serializer_class = ProductosSerializer
    permission_classes = [permissions.IsAuthenticated]

class FiadosViewSet(viewsets.ModelViewSet):
    queryset = Fiados.objects.all()
    serializer_class = FiadosSerializer
    permission_classes = [permissions.IsAuthenticated]

class ProductosPorFiadosViewSet(viewsets.ModelViewSet):
    queryset = ProductosPorFiados.objects.all()
    serializer_class = ProductosPorFiadosSerializer
    permission_classes = [permissions.IsAuthenticated]

class AuditoriasViewSet(viewsets.ModelViewSet):
    queryset = Auditorias.objects.all()
    serializer_class = AuditoriasSerializer
    permission_classes = [permissions.IsAuthenticated]
