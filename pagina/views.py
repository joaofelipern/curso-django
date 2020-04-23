from django.shortcuts import render, redirect
from django.conf import settings
from .forms import ContatoForm

def index(request):
    titulo = settings.SITE_TITLE
    return render(request, 'index.html', locals())

def contato(request):
    titulo = 'Contrate o nosso sistema'
    if request.method == 'POST':
        form = ContatoForm(request.POST)
        if form.is_valid():
            form.enviar_email()
            return redirect('/')
    else:
        form = ContatoForm()
    return render(request, 'contato.html', locals())