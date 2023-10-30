from django import forms
from .models import *

class AddQuot(forms.Form):
    title = forms.CharField(max_length=150),
    supplyer = forms.CharField(max_length=150),
    stavka= forms.CharField(max_length=50),
