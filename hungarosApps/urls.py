from django.urls import path, include
from rest_framework import routers
from .Api import (
    UsuariosViewSet, RolesViewSet, PermisosViewSet, PermisosPorRolesViewSet,
    TipoProductosViewSet, ProductosViewSet, FiadosViewSet, ProductosPorFiadosViewSet,
    AuditoriasViewSet
)

router = routers.DefaultRouter()
router.register('usuarios', UsuariosViewSet, basename='usuarios')
router.register('roles', RolesViewSet, basename='roles')
router.register('permisos', PermisosViewSet, basename='permisos')
router.register('permisos_por_roles', PermisosPorRolesViewSet, basename='permisos_por_roles')
router.register('tipo_productos', TipoProductosViewSet, basename='tipo_productos')
router.register('productos', ProductosViewSet, basename='productos')
router.register('fiados', FiadosViewSet, basename='fiados')
router.register('productos_por_fiados', ProductosPorFiadosViewSet, basename='productos_por_fiados')
router.register('auditorias', AuditoriasViewSet, basename='auditorias')

urlpatterns = [
    path('api/', include(router.urls)),
]
