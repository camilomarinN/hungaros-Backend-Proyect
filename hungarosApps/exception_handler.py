from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is None:
        return Response({
            "success": False,
            "message": "Error interno del servidor",
            "errors": str(exc)
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    # Manejo de ValidationError
    if isinstance(exc, ValidationError):
        return Response({
            "success": False,
            "message": "Error de validación",
            "errors": response.data
        }, status=response.status_code)

    # Otros errores DRF
    return Response({
        "success": False,
        "message": response.data.get("detail", "Ocurrió un error"),
        "errors": response.data
    }, status=response.status_code)
