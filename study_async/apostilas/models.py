from django.contrib.auth.models import User
from django.db import models


class Apostila(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    titulo = models.CharField(max_length=100)
    arquivo = models.FileField(upload_to='apostilas')
    tags = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.titulo
    
    def media_avaliacoes(self, tipo_avaliacao):
        avaliacoes = Avaliacao.objects.filter(apostila=self, avaliacao=tipo_avaliacao)
        if avaliacoes.exists():
            return avaliacoes.count()
        return 0


class ViewApostila(models.Model):
    ip = models.GenericIPAddressField()
    apostila = models.ForeignKey(Apostila, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.ip

class Avaliacao(models.Model):
    RUIM = 'RU'
    BOM = 'BO'
    OTIMO = 'OT'
    EXCELENTE = 'EX'

    ESCOLHAS_AVALIACAO = [
        (RUIM, 'Ruim'),
        (BOM, 'Bom'),
        (OTIMO, 'Ótimo'),
        (EXCELENTE, 'Excelente'),
    ]

    apostila = models.ForeignKey('Apostila', on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    avaliacao = models.CharField(max_length=2, choices=ESCOLHAS_AVALIACAO)

    def __str__(self):
        return f'{self.usuario.username} - {self.avaliacao}'


#implementar um model para avaliar a apostila. os choices da avaliacao poderao
#ser ruim,bom,ótimo,excelente
#a avaliação poderá ser então ruim, boa, ótima ou excelente
#implemente essa model aqui no models.py, implemente a logica de avaliar no views.py
#no template.html voce vai implementar uma div com o titulo: deixe sua avaliação
#em baixo terá um select com as opções de avaliação e embaixo tera um botão
#para avaliar a apostila selecionada na tela apostila.html.NO div tambem terá uma linha
#e logo abaixo um quantitativo de avaliações que aquela apostila recebeu e uma indicação em negrito indicando
#se a avaliação geral é ruim, boa, ótima ou excelente para isso ele precisa tirar
#a media de quantitativo de avaliações e mostrar a maior média geral para cada tipo de avaliação.
#faça isso na views.py crie tambem as devidas urls no urls.py

