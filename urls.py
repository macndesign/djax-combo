# coding=utf-8
from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', include('delivery.urls', namespace='delivery')),
    url(r'^address/$', include('address.urls', namespace='address')),
    url(r'^admin/', include(admin.site.urls)),
)
