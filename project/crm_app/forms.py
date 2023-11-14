from django import forms
from .models import *


class AddQuotForm(forms.ModelForm):
    class Meta:
        model = Quotation
        fields = ['descripsion', 'client', 'common_direction', 'common_transport', 'stavka1', 'comment_field1', 'stavka2', 'comment_field2', 'stavka3',
                  'comment_field3', 'stavka4', 'comment_field4', 'stavka5', 'comment_field5', 'stavka6', 'comment_field6', 'stavka7', 'comment_field7',
                  'stavka8', 'comment_field8', 'stavka9', 'comment_field9', 'stavka10', 'comment_field10', 'status', 'result',]
        widgets = {
            'descripsion': forms.Textarea(attrs={'cols': 40, 'rows': 2}),
            'comment_field1': forms.Textarea(attrs={'cols': 40, 'rows': 8}),
            'comment_field2': forms.Textarea(attrs={'cols': 40, 'rows': 8}),
            'comment_field3': forms.Textarea(attrs={'cols': 40, 'rows': 8}),
            'comment_field4': forms.Textarea(attrs={'cols': 40, 'rows': 8}),
            'comment_field5': forms.Textarea(attrs={'cols': 40, 'rows': 8}),
            'comment_field6': forms.Textarea(attrs={'cols': 40, 'rows': 8}),
            'comment_field7': forms.Textarea(attrs={'cols': 40, 'rows': 8}),
            'comment_field8': forms.Textarea(attrs={'cols': 40, 'rows': 8}),
            'comment_field9': forms.Textarea(attrs={'cols': 40, 'rows': 8}),
            'comment_field10': forms.Textarea(attrs={'cols': 40, 'rows': 8}),

        }