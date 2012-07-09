# coding=utf-8
from django import forms
from address.models import Estado, Cidade, Bairro

class EnderecoForm(forms.Form):
    estado = forms.ModelChoiceField(
        empty_label="Selecione ...",
        queryset = Estado.objects.all(),
    )
    cidade = forms.ChoiceField(choices=(("0", ""),))
    bairro = forms.ChoiceField(choices=(("0", ""),))
