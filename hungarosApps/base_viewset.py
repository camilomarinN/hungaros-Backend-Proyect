from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema
from .serializers import StandardResponseSerializer, ErrorResponseSerializer


class BaseModelViewSet(ModelViewSet):
    
    # ===================== RESPUESTAS BASE ======================

    def success_response(self, message, data=None, status_code=status.HTTP_200_OK):
        return Response({
            "success": True,
            "message": message,
            "data": data
        }, status=status_code)

    def error_response(self, message, errors=None, status_code=status.HTTP_400_BAD_REQUEST):
        return Response({
            "success": False,
            "message": message,
            "errors": errors
        }, status=status_code)

    def get_model_name(self):
        return self.get_queryset().model._meta.verbose_name.capitalize()

    # ===================== CREATE GLOBAL ========================

    @extend_schema(
        responses={
            201: StandardResponseSerializer,
            400: ErrorResponseSerializer
        }
    )
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        return self.success_response(
            f"{self.get_model_name()} creado correctamente",
            serializer.data,
            status.HTTP_201_CREATED
        )

    # ===================== UPDATE GLOBAL ========================

    @extend_schema(
        responses={
            200: StandardResponseSerializer,
            400: ErrorResponseSerializer
        }
    )
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return self.success_response(
            f"{self.get_model_name()} actualizado correctamente",
            serializer.data
        )

    # ===================== DELETE GLOBAL ========================

    @extend_schema(
        responses={
            200: StandardResponseSerializer
        }
    )
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)

        return self.success_response(
            f"{self.get_model_name()} eliminado correctamente"
        )

    # ===================== RETRIEVE GLOBAL ======================

    @extend_schema(
        responses={
            200: StandardResponseSerializer
        }
    )
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)

        return self.success_response(
            f"{self.get_model_name()} obtenido correctamente",
            serializer.data
        )

    # ===================== LIST GLOBAL ==========================

    @extend_schema(
        responses={
            200: StandardResponseSerializer
        }
    )
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)

        return self.success_response(
            f"Lista de {self.get_model_name()} obtenida correctamente",
            serializer.data
        )
