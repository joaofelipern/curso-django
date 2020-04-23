from django import forms
from .models import MovRotativo

class CheckinRotativoForm(forms.ModelForm):

    class Meta:
        model = MovRotativo
        # fields = '__all__'
        fields = ('checkin', 'veiculo')


class CheckoutRotativoForm(forms.ModelForm):
    class Meta:
        model = MovRotativo
        # fields = '__all__'
        fields = ('checkout', 'pago')        