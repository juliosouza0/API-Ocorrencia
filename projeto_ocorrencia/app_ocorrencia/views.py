from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Ocorrencia
from .serializers import OcorrenciaSerializer
from rest_framework.parsers import MultiPartParser, FormParser

class OcorrenciaViewSet(viewsets.ModelViewSet):
    queryset = Ocorrencia.objects.all()
    serializer_class = OcorrenciaSerializer
    parser_classes = (MultiPartParser, FormParser)