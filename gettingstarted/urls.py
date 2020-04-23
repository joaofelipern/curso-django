from django.urls import path, include
from django.contrib import admin
from django.conf import settings

admin.autodiscover()

import hello.views
import estacionamento

# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/

urlpatterns = [
    # path("", hello.views.index, name="index"),
    # path("db/", hello.views.db, name="db"),
    # path("admin/", admin.site.urls),
    
    path('estacionamento/', include('estacionamento.urls')),
    path("admin/", admin.site.urls),  # manda pro admin
]


admin.site.site_title = settings.SITE_TITLE
admin.site.site_header = settings.SITE_HEADER
admin.site.index_title = settings.INDEX_TITLE