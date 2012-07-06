from django.db import models
from address.forms import EnderecoForm

class Endereco(object):
    def __init__(self, estado=None, cidade=None, bairro=None):
        self.estado = estado
        self.cidade = cidade
        self.bairro = bairro

    def get_form(self):
        form = EnderecoForm()

        form.fields['estado'].initial = self.estado.pk

        cidades = self.estado.cidade_set.all()
        form.fields['cidade'].queryset = cidades

        form.fields['cidade'].initial = self.cidade

        bairros = self.cidade.bairro_set.all()
        form.fields['bairro'].queryset = bairros

        form.fields['bairro'].initial = self.bairro

        return form


class Estado(models.Model):
    sigla = models.CharField(max_length=2)
    
    class Meta:
        ordering = ['sigla']
    
    @property
    def cidades(self):
        cidades = self.cidade_set.all()
        clist = []
        
        for cidade in cidades:
            clist.append(
                {'pk': cidade.pk, 'nome': cidade.nome}
            )
            
        return clist

    def __unicode__(self):
        return self.sigla
    
    def as_dict(self):
        return {
            'pk': self.pk,
            'sigla': self.sigla,
            'cidades': list(self.cidades),
        }


class Cidade(models.Model):
    nome = models.CharField(max_length=75)
    estado = models.ForeignKey('Estado')
    
    class Meta:
        ordering = ['nome']
    
    @property
    def bairros(self):
        bairros = self.bairro_set.all()
        blist = []
        
        for bairro in bairros:
            blist.append(
                {'pk': bairro.pk, 'nome': bairro.nome}
            )
            
        return blist

    def __unicode__(self):
        return self.nome
    
    def as_dict(self):
        return {
            'pk': self.pk,
            'nome': self.nome,
            'pk_estado': self.estado.pk,
            'bairros': list(self.bairros),
        }


class Bairro(models.Model):
    nome = models.CharField(max_length=120)
    cidade = models.ForeignKey('Cidade')

    def __unicode__(self):
        return self.nome
    
    def as_dict(self):
        return {
            'pk': self.pk,
            'nome': self.nome,
            'pk_cidade': self.cidade.pk,
        }
