from django.db import models
from address.models import Estado, Cidade, Bairro

class Estabelecimento(models.Model):
    nome = models.CharField(max_length=75)
    estado = models.ForeignKey(Estado)
    cidade = models.ForeignKey(Cidade)
    bairro = models.ForeignKey(Bairro)

    def __unicode__(self):
        return self.nome

    def as_dict(self):
        return {
            'pk': self.pk,
            'nome': self.nome,
            'pk_estado': self.estado.pk,
            'pk_cidade': self.cidade.pk,
            'pk_bairro': self.bairro.pk,
            }


class LocalEntrega(models.Model):
    estabelecimento = models.ForeignKey('Estabelecimento')
    bairro = models.ForeignKey(Bairro)

    def __unicode__(self):
        return "%s, %s" % (self.estabelecimento.nome, self.bairro.nome)

    def as_dict(self):
        return {
            'pk': self.pk,
            'pk_estabelecimento': self.estabelecimento.pk,
            'pk_bairro': self.bairro.pk,
        }
