# coding=utf-8
# Create your views here.
from django.shortcuts import render
from address.forms import EnderecoForm
from delivery.models import Estabelecimento

def base(request):
    return render(request, 'base.html')


def home(request):
    form = EnderecoForm()
    context = {'form': form}

    try:
        endereco = request.session['endereco']
        bairro = endereco.bairro
        locais_entrega = bairro.localentrega_set.all()

        estabelecimentos = Estabelecimento.objects.filter(
            pk__in=[i.estabelecimento.pk for i in locais_entrega]
        ).order_by('nome')

        form = request.session['endereco'].get_form()

    except KeyError:
        estabelecimentos = []

    context.update({
        'form': form,
        'estabelecimentos': estabelecimentos,
    })

    return render(request, 'delivery/home.html', context)