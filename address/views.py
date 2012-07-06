from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404, redirect
from address.models import Estado, Cidade, Bairro
from address.utils import Endereco

def confirmar_endereco(request):
    endereco = Endereco()

    if ('estado' and 'cidade' and 'bairro') in request.POST:
        try:
            endereco.estado = get_object_or_404(Estado, pk=request.POST['estado'])
            endereco.cidade = get_object_or_404(Cidade, pk=request.POST['cidade'])
            endereco.bairro = get_object_or_404(Bairro, pk=request.POST['bairro'])

            request.session['endereco'] = endereco

        except ValueError:
            return redirect(reverse('home'))

    return redirect(reverse('home'))


def remover_endereco(request):
    if 'endereco' in request.session:
        del  request.session['endereco']

    return redirect(reverse('home'))
