from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from .models import *


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class ': 'form-input'})),
    email= forms.EmailField(label='email', widget=forms.EmailInput(attrs={'class ': 'form-input'})),
    password1= forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'})),
    password2= forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-input'})),

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class ': 'form-input'})),
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'})),





class AddTimePeriod(forms.ModelForm):
    class Meta:
        model = TimePeriod
        fields = '__all__'

#===========================================
class UploadDocumentsForm(forms.ModelForm):
    class Meta:
        model = Documents
        fields = ['name', 'client', 'sdelka', 'supplyer', 'other_company', 'type', 'file']

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