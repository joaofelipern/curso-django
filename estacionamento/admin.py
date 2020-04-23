from django.contrib import admin
from .models import Marca, Pessoa, Veiculo, MovRotativo, Parametro, Mensalista, MovMensalista
from .forms import CheckinRotativoForm, CheckoutRotativoForm


admin.site.register(Marca)
admin.site.register(Pessoa)
admin.site.register(Veiculo)


class MovMensalistaAdmin(admin.ModelAdmin):
    list_display = ('mensalista', 'data_pagamento')

admin.site.register(MovMensalista, MovMensalistaAdmin)


class MensalistaAdmin(admin.ModelAdmin):
    list_display = ('veiculo', '_proprietario', 'inicio', 'valor_mensal')

    def _proprietario(self, obj):
        return obj.veiculo.proprietario


admin.site.register(Mensalista, MensalistaAdmin)





class MovRotativoAdmin(admin.ModelAdmin):
    list_display = ('checkin', 'checkout', 'valor_hora', 'veiculo', 'pago', 'valor')

    # def get_form(self, request, obj=None, **kwargs):
    #     if obj is None:
    #         return CheckinRotativoForm
    #     else:
    #         return CheckoutRotativoForm
    #     return super(MovRotativoAdmin, self).get_form(request, obj, **kwargs)

admin.site.register(MovRotativo, MovRotativoAdmin)


class ParametroAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if not Parametro.objects.exists():
            return True
        return False

admin.site.register(Parametro, ParametroAdmin)