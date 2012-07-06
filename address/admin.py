from django.contrib import admin
from address.models import Estado, Cidade, Bairro

admin.site.register(Estado)
admin.site.register(Cidade)
admin.site.register(Bairro)
