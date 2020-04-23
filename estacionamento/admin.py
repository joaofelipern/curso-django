from django.contrib import admin
from .models import Marca, Pessoa, Veiculo, MovRotativo, Parametro

admin.site.register(Marca)
admin.site.register(Pessoa)
admin.site.register(Veiculo)





class MovRotativoAdmin(admin.ModelAdmin):
    list_display = ('checkin', 'checkout', 'valor_hora', 'veiculo', 'pago', 'valor')

admin.site.register(MovRotativo, MovRotativoAdmin)


class ParametroAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if not Parametro.objects.exists():
            return True
        return False

admin.site.register(Parametro, ParametroAdmin)