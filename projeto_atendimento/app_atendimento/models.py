from django.db import models

# Create your models here.
class Atendimento(models.Model):
    # Opções de turma
    TURMA_OPCOES = [
        ("1_ADM", "1º Ano de Administração"),
        ("2_ADM", "2º Ano de Administração"),
        ("1_INF", "1º Ano de Informática"),
        ("2_INF", "2º Ano de Informática"),
        ("3_INF", "3º Ano de Informática"),
        ("SUB_ADM", "Administração Subsequente"),
        ("SUB_INF", "Informática Subsequente"),
        ("SUB_SEC", "Secretariado Subsequente"),
    ]

    # Opções de despacho
    DESPACHO_OPCOES = [
        ("NUE", "NUE"),
        ("CD", "Comissão Disciplinar"),
    ]

    discente = models.CharField(max_length=100)
    matricula = models.CharField(max_length=20, unique=True)
    turma = models.CharField(max_length=10, choices=TURMA_OPCOES)
    data_atendimento = models.DateField()
    despacho_cae = models.CharField(max_length=3, choices=DESPACHO_OPCOES)
    evidencias = models.FileField(upload_to='evidencias/', blank=True, null=True)
    motivo = models.CharField(max_length=255)
    descricao_ocorrencia = models.TextField()

    def __str__(self):
        return f"{self.matricula} - {self.get_turma_display()}"
