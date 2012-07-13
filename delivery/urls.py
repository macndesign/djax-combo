# coding=utf-8
from django.conf.urls import patterns, url
from core.api.json_response import JSONDetailView
from delivery.models import Estabelecimento, LocalEntrega

urlpatterns = patterns('delivery.views',
    url(r'^$', 'base', name='base'),
    url(r'^home/$', 'home', name='home'),
)

urlpatterns += patterns('',
    # JSON
    url(r'^estabelecimento/(?P<pk>\d)$', JSONDetailView.as_view(model=Estabelecimento)),
    url(r'^local-entrega/(?P<pk>\d)$', JSONDetailView.as_view(model=LocalEntrega)),
)
