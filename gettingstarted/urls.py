from django.urls import path, include
from django.contrib import admin
from django.conf import settings

admin.autodiscover()

import estacionamento
import pagina

urlpatterns = [
    path('', include('pagina.urls')),
    path('estacionamento/', include('estacionamento.urls')),
    path('admin/', admin.site.urls),
]

admin.site.site_title = settings.SITE_TITLE
admin.site.site_header = settings.SITE_HEADER
admin.site.index_title = settings.INDEX_TITLE