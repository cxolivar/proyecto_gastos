from django.urls import path
from .views import GastosAPIView, GastoDetailAPIView

urlpatterns = [
    # /api/gastos/ -> GET (listar), POST (crear)
    path("gastos/", GastosAPIView.as_view(), name="gastos_list_create"),
    # /api/gastos/<id>/ -> GET (detalle), PUT (actualizar), DELETE (eliminar)
    path("gastos/<int:id>/", GastoDetailAPIView.as_view(), name="gasto_detail"),
]
