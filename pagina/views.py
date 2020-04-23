from django.shortcuts import render
from django.conf import settings

def index(request):
    titulo = settings.SITE_TITLE
    return render(request, 'index.html', locals())