# coding=utf-8
from django.conf.urls import patterns, url
from address.models import Estado, Cidade, Bairro
from api.json_response import JSONDetailView

urlpatterns = patterns('address.views',
    url(r'^confirmar-endereco/$', 'confirmar_endereco', name='confirmar-endereco'),
    url(r'^remover-endereco/$', 'remover_endereco', name='remover-endereco'),

    # JSON
    url(r'^estado/(?P<pk>\d)$', JSONDetailView.as_view(model=Estado), name="estado"),
    url(r'^cidade/(?P<pk>\d)$', JSONDetailView.as_view(model=Cidade), name="cidade"),
    url(r'^bairro/(?P<pk>\d)$', JSONDetailView.as_view(model=Bairro), name="bairro"),
)
