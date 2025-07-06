from django.urls import path
from .views import (
    SolicitacaoListCreateAPIView,
    SolicitacaoRetrieveUpdateDestroyAPIView,
)

urlpatterns = [
    path('solicitacoes/', SolicitacaoListCreateAPIView.as_view(), name='solicitacao-list-create'),
    path('solicitacoes/<int:pk>/', SolicitacaoRetrieveUpdateDestroyAPIView.as_view(), name='solicitacao-detalhe'),
]