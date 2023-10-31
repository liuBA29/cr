from django import forms
from .models import *

class SdelkaForm(forms.ModelForm):
    class Meta:
        model = Sdelka
        fields = '__all__'

    date = forms.DateInput()

class StavkaForm(forms.ModelForm):
    class Meta:
        model = Stavka
        fields = '__all__'