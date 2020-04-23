from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import MovRotativoForm


def adicionar_movimento_rotativo(request):
    if request.method == 'POST':
        form = MovRotativoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/admin/estacionamento/movrotativo/', 'Salvo com sucesso')
    else:
        form = MovRotativoForm()
    print (dir(form))
    return render(request, 'change_form.html', locals())