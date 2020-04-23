from django import forms
from .models import MovRotativo

class MovRotativoForm(forms.ModelForm):
    class Meta:
        model = MovRotativo
        fields = '__all__'