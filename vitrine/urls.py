from django.urls import path

from .views import ProdutosDetail, ProdutosList


urlpatterns = [
    # produtos
    path('vitrine/produtos/', ProdutosList.as_view(), name='produtos-list'),
    path('vitrine/produtos/<int:pk>/', ProdutosDetail.as_view(), name='produtos-detail'),

]
