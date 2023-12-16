from django import forms
from .models import *


class UploadDocumentsForm(forms.ModelForm):
    class Meta:
        model = Documents
        fields = ['name', 'client', 'sdelka','supplyer',  'type', 'file']

class DocumentSdelkaClientForm(forms.ModelForm):
    class Meta:
        model = Documents
        fields = ['name', 'client', 'supplyer', 'sdelka', 'type', 'file']


class DocumentSdelkaSupplyerForm(forms.ModelForm):
    class Meta:
        model = Documents
        fields = ['name', 'client', 'supplyer', 'sdelka', 'type', 'file']



class AddClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'

class SearchSupplyerForm(forms.Form):
    date_from = forms.CharField()
    date_to = forms.CharField()

class AddSupplyerForm(forms.ModelForm):
    class Meta:
        model = Supplyer
        fields = '__all__'


class AddOtherCompanyForm(forms.ModelForm):
    class Meta:
        model = OtherCompany
        fields = '__all__'

#============================================================


class AddSdelkaForm(forms.ModelForm):
    class Meta:
        model = Sdelka
        fields = '__all__'



class AddQuotForm(forms.ModelForm):
    class Meta:
        model = Quotation
        fields = ['description', 'client', 'loading_country', 'unloading_country', 'common_transport', 'supplyer_1', 'sup_price_1', 'currency1', 'comment_field1',
                  'supplyer_2', 'sup_price_2', 'currency2', 'comment_field2', 'supplyer_3', 'sup_price_3', 'currency3', 'comment_field3', 'supplyer_4', 'sup_price_4', 'currency4',
                  'comment_field4', 'supplyer_5', 'sup_price_5', 'currency5', 'comment_field5', 'supplyer_6', 'sup_price_6', 'currency6', 'comment_field6',
                  'supplyer_7', 'sup_price_7', 'currency7', 'comment_field7', 'supplyer_8', 'sup_price_8', 'currency8', 'comment_field8', 'supplyer_9', 'sup_price_9',
                  'currency9', 'comment_field9', 'supplyer_10','sup_price_10', 'currency10',  'comment_field10', 'status', 'result', ]
        widgets = {
            'description': forms.Textarea(attrs={'cols': 40, 'rows': 2}),

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