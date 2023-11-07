from django import forms
from .models import *


class AddQuotForm(forms.Form):
    descripsion = forms.CharField(max_length=150, required=False, label='Описание потребности',
                                  widget=forms.TextInput(attrs={'class':'form-input'}))
    transport = forms.CharField( max_length=20, label='Транспорт')

    client = forms.ModelChoiceField(queryset=Client.objects.all(), label='Заказчик')
    common_direction = forms.CharField(max_length=20, required=False, label='общее направленіе доставкі')
    common_transport = forms.CharField(max_length=20, required=False, label='Транспорт іспользуемый - весь')

    stavka1 = forms.CharField(max_length=20, required=False, label='ставка1')
    comment_field1 = forms.CharField(max_length=20, required=False, label='комментарій к ставке1',
                                     widget=forms.TextInput(attrs={'class':'block'}))

    stavka2 = forms.CharField(max_length=20, required=False, label='ставка2',
                              widget=forms.TextInput(attrs={'class':'block'}))
    comment_field2 = forms.CharField(max_length=20, required=False, label='комментарій к ставке2',
                                     widget=forms.TextInput(attrs={'class':'block'}))

    stavka3 = forms.CharField(max_length=20, required=False, label='ставка3')
    comment_field3 = forms.CharField(max_length=20, required=False, label='комментарій к ставке3')

    stavka4 = forms.CharField(max_length=20, required=False, label='ставка4')
    comment_field4 = forms.CharField(max_length=20, required=False, label='комментарій к ставке4')

    status = forms.CharField(max_length=20, initial='новая', label='статус: новая, в работе, закрыта')

    result = forms.CharField(max_length=20,initial='груз не готов',
                              label='статус2: прошли по цене, груз не готов, не прошли по цене')

