from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, serializers
from drf_spectacular.utils import extend_schema, OpenApiExample
from .models import Usuarios
from hungarosApps.security_utils import verify_password

class LoginSerializer(serializers.Serializer):
    id_usuario = serializers.CharField()
    password = serializers.CharField(write_only=True)


class LoginResponseSerializer(serializers.Serializer):
    message = serializers.CharField()
    usuario = serializers.DictField()

class LoginView(APIView):
    @extend_schema(
        request=LoginSerializer,
        responses={
            200: LoginResponseSerializer,
            401: OpenApiExample(
                'Credenciales inválidas',
                summary="Error de autenticación",
                value={"error": "Contraseña incorrecta"},
                status_codes=["401"]
            ),
            404: OpenApiExample(
                'Usuario no encontrado',
                value={"error": "Usuario no encontrado"},
                status_codes=["404"]
            )
        },
        description="Endpoint para iniciar sesión de usuario y validar credenciales."
    )
    def post(self, request):
        id_usuario = request.data.get('id_usuario')
        password = request.data.get('password')

        if not id_usuario or not password:
            return Response(
                {"error": "Debe proporcionar id_usuario y password"},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            user = Usuarios.objects.get(id_usuario=id_usuario)
        except Usuarios.DoesNotExist:
            return Response(
                {"error": "Usuario no encontrado"},
                status=status.HTTP_404_NOT_FOUND
            )

        if verify_password(user.hash_contrasena_usu, password):
            return Response({
                "message": "Login exitoso",
                "usuario": {
                    "id_usuario": user.id_usuario,
                    "nombre": user.nombre_usu,
                    "rol": user.id_rol.nombre_rol
                }
            }, status=status.HTTP_200_OK)
        else:
            return Response(
                {"error": "Contraseña incorrecta"},
                status=status.HTTP_401_UNAUTHORIZED
            )
