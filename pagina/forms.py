from django import forms
from django.conf import settings
from django.core.mail import send_mail

class ContatoForm(forms.Form):
    nome = forms.CharField(max_length=30)
    email = forms.EmailField()
    mensagem = forms.CharField(widget=forms.Textarea())

    def enviar_email(self):
        mensagem = self.cleaned_data['mensagem']
        remetente = self.cleaned_data['email']
        try:
            send_mail(
                'Contato no site',
                mensagem,
                remetente,
                ['administrador@gmail.comm'],
                fail_silently=False,
            )
            return True
        except:
            return False