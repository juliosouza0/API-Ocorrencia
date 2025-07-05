from django.db import models

class Ocorrencia(models.Model):
    DESPACHO_CHOICES = [
        ('NUE', 'NUE'),
        ('COMISSAO', 'Comissão Disciplinar'),
    ]

    id = models.AutoField(primary_key=True)
    discente = models.CharField(max_length=100)
    alunos_envolvidos = models.TextField()
    matricula = models.CharField(max_length=20)
    curso = models.CharField(max_length=100)
    data_registro = models.DateTimeField(auto_now_add=True)
    data_ocorrencia = models.DateField()
    hora = models.TimeField()
    local_ocorrencia = models.CharField(max_length=200)
    atitudes_inadequadas = models.TextField()
    envolvidos_ocorrencia = models.TextField()
    relato_ocorrencia = models.TextField()
    evidencias = models.FileField(upload_to='evidencias/', blank=True, null=True)
    ha_testemunhas = models.BooleanField(default=False)

    despacho_cae = models.CharField(
        max_length=20,
        choices=DESPACHO_CHOICES,
        default='NUE',
        verbose_name='Despacho do CAE'
    )

    observacoes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Ocorrência do(a) {self.discente} em {self.data_ocorrencia}"
