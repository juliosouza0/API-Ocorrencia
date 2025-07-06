from rest_framework import generics
from .models import Solicitacao
from .serializers import SolicitacaoSerializer

class SolicitacaoListCreateAPIView(generics.ListCreateAPIView):
    queryset = Solicitacao.objects.all()
    serializer_class = SolicitacaoSerializer

class SolicitacaoRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Solicitacao.objects.all()
    serializer_class = SolicitacaoSerializer