# coding=utf-8
from django import forms
from address.models import Estado, Cidade, Bairro

class EnderecoForm(forms.Form):
    estado = forms.ModelChoiceField(
        empty_label="-- Selecione --",
        queryset = Estado.objects.all(),
    )

    cidade = forms.ModelChoiceField(
        empty_label="-- Vazio --",
        queryset = Cidade.objects.all()[:1],
    )

    bairro = forms.ModelChoiceField(
        empty_label="-- Vazio --",
        queryset = Bairro.objects.all()[:1],
    )
