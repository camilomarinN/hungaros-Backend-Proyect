from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, serializers
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from drf_spectacular.utils import extend_schema

from .serializers import ErrorResponseSerializer
from .auth_services import authenticate_user, create_single_session_token


# ============================================================
# ===================== REQUEST SERIALIZER ===================
# ============================================================

class LoginSerializer(serializers.Serializer):
    id_usuario = serializers.CharField()
    password = serializers.CharField(write_only=True)


# ============================================================
# ===================== RESPONSE SERIALIZERS =================
# ============================================================

class LoginUserSerializer(serializers.Serializer):
    id_usuario = serializers.CharField()
    nombre = serializers.CharField()
    rol = serializers.CharField()


class LoginResponseSerializer(serializers.Serializer):
    success = serializers.BooleanField()
    message = serializers.CharField()
    token = serializers.CharField()
    usuario = LoginUserSerializer()


# ============================================================
# ===================== LOGIN VIEW ===========================
# ============================================================

class LoginView(APIView):
    permission_classes = [AllowAny]

    @extend_schema(
        request=LoginSerializer,
        responses={
            200: LoginResponseSerializer,
            400: ErrorResponseSerializer,
            401: ErrorResponseSerializer,
            500: ErrorResponseSerializer,
        },
        description="""
        Endpoint de login.

        - Valida credenciales
        - Soporta usuarios legacy
        - Migra contraseñas a Argon2 automáticamente
        - Garantiza una sola sesión activa por usuario
        """
    )
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        id_usuario = serializer.validated_data["id_usuario"].strip()
        password = serializer.validated_data["password"]

        usuario = authenticate_user(id_usuario, password)

        if not usuario:
            return Response(
                {
                    "success": False,
                    "message": "Credenciales inválidas",
                    "errors": None
                },
                status=status.HTTP_401_UNAUTHORIZED
            )

        token = create_single_session_token(usuario)

        return Response(
            {
                "success": True,
                "message": "Login exitoso",
                "token": token.key,
                "usuario": {
                    "id_usuario": usuario.id_usuario,
                    "nombre": usuario.nombre_usu,
                    "rol": usuario.id_rol.nombre_rol,
                }
            },
            status=status.HTTP_200_OK
        )


# ============================================================
# ===================== LOGOUT VIEW ==========================
# ============================================================

class LogoutResponseSerializer(serializers.Serializer):
    success = serializers.BooleanField()
    message = serializers.CharField()


class LogoutView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    @extend_schema(
        responses={200: LogoutResponseSerializer}
    )
    def post(self, request):
        request.auth.delete()

        return Response(
            {
                "success": True,
                "message": "Sesión cerrada correctamente"
            },
            status=status.HTTP_200_OK
        )