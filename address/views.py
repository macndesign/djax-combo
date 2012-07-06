from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404, redirect
from address.forms import EnderecoForm
from address.models import Estado, Cidade, Bairro

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


def confirmar_endereco(request):
    endereco = Endereco()

    if ('estado' and 'cidade' and 'bairro') in request.POST:
        try:
            endereco.estado = get_object_or_404(Estado, pk=request.POST['estado'])
            endereco.cidade = get_object_or_404(Cidade, pk=request.POST['cidade'])
            endereco.bairro = get_object_or_404(Bairro, pk=request.POST['bairro'])

            request.session['endereco'] = endereco

        except ValueError:
            return redirect(reverse('delivery:home'))

    return redirect(reverse('delivery:home'))


def remover_endereco(request):
    if 'endereco' in request.session:
        del  request.session['endereco']

    return redirect(reverse('delivery:home'))
