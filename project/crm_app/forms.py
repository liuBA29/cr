from django import forms
from .models import *


class AddQuotForm(forms.ModelForm):
    class Meta:
        model = Quotation
        fields = ['descripsion', 'client', 'loading_country', 'unloading_country', 'common_transport', 'stavka1', 'price1', 'currency1', 'comment_field1',
                  'stavka2', 'price2', 'currency2', 'comment_field2', 'stavka3', 'price3', 'currency3', 'comment_field3', 'stavka4', 'price4', 'currency4',
                  'comment_field4', 'stavka5', 'price5', 'currency5', 'comment_field5', 'stavka6', 'price6', 'currency6', 'comment_field6',
                  'stavka7', 'price7', 'currency7', 'comment_field7', 'stavka8', 'price8', 'currency8', 'comment_field8', 'stavka9', 'price9',
                  'currency9', 'comment_field9', 'stavka10','price10', 'currency10',  'comment_field10', 'status', 'result', ]
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