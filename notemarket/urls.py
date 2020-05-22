from django.urls import path

from .views import ProdutosDetail, ProdutosList


urlpatterns = [
    # produtos
    path('notemarket/produtos/', ProdutosList.as_view(), name='produtos-list'),
    path('notemarket/produtos/<int:pk>/', ProdutosDetail.as_view(), name='produtos-detail'),

]
