from django.urls import path

from .views import InventarioDetail, InventarioList


urlpatterns = [
    # inventario
    path('notemarket/inventario/', InventarioList.as_view(), name='inventario-list'),
    path('notemarket/inventario/<int:pk>/', InventarioDetail.as_view(), name='inventario-detail'),

]
