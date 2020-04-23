from django.contrib import admin
from .models import Marca, Pessoa, Veiculo, MovRotativo, Parametro, Mensalista, MovMensalista

admin.site.register(Marca)
admin.site.register(Pessoa)
admin.site.register(Veiculo)


class MovMensalistaAdmin(admin.ModelAdmin):
    list_display = ('mensalista', 'data_pagamento')

admin.site.register(MovMensalista, MovMensalistaAdmin)


class MensalistaAdmin(admin.ModelAdmin):
    list_display = ('veiculo', 'inicio', 'valor_mensal')

admin.site.register(Mensalista, MensalistaAdmin)





class MovRotativoAdmin(admin.ModelAdmin):
    list_display = ('checkin', 'checkout', 'valor_hora', 'veiculo', 'pago', 'valor')

admin.site.register(MovRotativo, MovRotativoAdmin)


class ParametroAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if not Parametro.objects.exists():
            return True
        return False

admin.site.register(Parametro, ParametroAdmin)