from django.db import models

# Create your models here.
class Solicitacao(models.Model):

    class Turmas(models.TextChoices):
        ADM1   = "ADM1", "1º ano de Administração"
        ADM2   = "ADM2", "2º ano de Administração"
        INF1   = "INF1", "1º ano de Informática"
        INF2   = "INF2", "2º ano de Informática"
        INF3   = "INF3", "3º ano de Informática"
        ADMSUB = "ADMSUB", "Administração subsequente"
        INFSUB = "INFSUB", "Informática subsequente"
        SECSUB = "SECSUB", "Secretariado subsequente"

    id = models.AutoField(primary_key=True)          
    discente = models.CharField(max_length=100)      
    turma = models.CharField(                        
        max_length=6,
        choices=Turmas.choices
    )
    data = models.DateField()                        
    mensagem = models.TextField(                     
        verbose_name="Solicitação ou dúvida"
    )
    criado_em = models.DateTimeField(               
        auto_now_add=True
    )
    atualizado_em = models.DateTimeField(            
        auto_now=True
    )

    def __str__(self):
        return f"{self.discente} - {self.get_turma_display()} - {self.data:%Y-%m-%d}"