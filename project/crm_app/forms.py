from django import forms
from .models import *


class AddQuotForm(forms.ModelForm):
    class Meta:
        model = Quotation
        fields = '__all__'