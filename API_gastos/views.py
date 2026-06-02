from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Gasto
from .serializers import GastoSerializer

class GastosAPIView(APIView):
    """
    API para listar y crear gastos.
    """
    def get(self, request):
        # Obtenemos todos los registros o filtramos por tipo si se proporciona
        tipo = request.query_params.get('tipo', None)
        if tipo:
            gastos = Gasto.objects.filter(tipo__iexact=tipo)
        else:
            gastos = Gasto.objects.all()

        serializer = GastoSerializer(gastos, many=True)
        return Response(serializer.data)

    def post(self, request):
        # La validación de campos requeridos ahora la hace el serializador
        serializer = GastoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GastoDetailAPIView(APIView):
    """
    API para obtener, actualizar y eliminar un gasto específico.
    """
    def get_object(self, id):
        # Usamos get_object_or_404 para manejar el error si no se encuentra
        return get_object_or_404(Gasto, id=id)

    def get(self, request, id):
        gasto = self.get_object(id)
        serializer = GastoSerializer(gasto)
        return Response(serializer.data)

    def put(self, request, id):
        gasto = self.get_object(id)
        serializer = GastoSerializer(gasto, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        gasto = self.get_object(id)
        gasto.delete()
        return Response({"mensaje": "Gasto eliminado correctamente"}, status=status.HTTP_204_NO_CONTENT)