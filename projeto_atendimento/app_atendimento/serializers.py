from rest_framework import serializers
from .models import Atendimento

class AtendimentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Atendimento
        fields = '__all__'  # ou liste os campos incluindo 'discente'