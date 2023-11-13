from django import forms
from .models import *


class AddQuotForm(forms.Form):
    descripsion = forms.CharField(max_length=250, required=False, label='Описание потребности',
                                  widget=forms.TextInput(attrs={'class':'form-input'}))
    client = forms.ModelChoiceField(queryset=Client.objects.all(), label='Заказчик')

    transport = forms.CharField( max_length=20, label='Транспорт')


    common_direction = forms.CharField(max_length=20, required=False, label='общее направленіе доставкі')
    common_transport = forms.CharField(max_length=20, required=False, label='Транспорт іспользуемый - весь')

    stavka1 = forms.CharField(max_length=20, required=False, label='Перевозчик 1')
    comment_field1 = forms.CharField(max_length=280, required=False, label='Комментарий к ставке 1',
                                     widget=forms.TextInput(attrs={'class':'block'}))

    stavka2 = forms.CharField(max_length=20, required=False, label='ставка2',
                              widget=forms.TextInput(attrs={'class':'block'}))
    comment_field2 = forms.CharField(max_length=280, required=False, label='комментарій к ставке2',
                                     widget=forms.TextInput(attrs={'class':'block'}))

    stavka3 = forms.CharField(max_length=20, required=False, label='ставка3')
    comment_field3 = forms.CharField(max_length=280, required=False, label='комментарій к ставке3')

    stavka4 = forms.CharField(max_length=20, required=False, label='ставка4')
    comment_field4 = forms.CharField(max_length=280, required=False, label='комментарій к ставке4')

    stavka5 = forms.CharField(max_length=20, required=False, label='ставка5',
                              widget=forms.TextInput(attrs={'class': 'block'}))
    comment_field5 = forms.CharField(max_length=280, required=False, label='комментарій к ставке5',
                                     widget=forms.TextInput(attrs={'class': 'block'}))

    stavka6 = forms.CharField(max_length=20, required=False, label='ставка6')
    comment_field6 = forms.CharField(max_length=280, required=False, label='комментарій к ставке6')

    stavka7 = forms.CharField(max_length=20, required=False, label='ставка7')
    comment_field7 = forms.CharField(max_length=280, required=False, label='комментарій к ставке7')

    stavka8 = forms.CharField(max_length=20, required=False, label='ставка8',
                              widget=forms.TextInput(attrs={'class': 'block'}))
    comment_field8 = forms.CharField(max_length=280, required=False, label='комментарій к ставке8',
                                     widget=forms.TextInput(attrs={'class': 'block'}))

    stavka9 = forms.CharField(max_length=20, required=False, label='ставка9')
    comment_field9 = forms.CharField(max_length=280, required=False, label='комментарій к ставке9')

    stavka10 = forms.CharField(max_length=20, required=False, label='ставка10')
    comment_field10 = forms.CharField(max_length=280, required=False, label='комментарій к ставке10')

    status = forms.CharField(max_length=20, initial='новая', label='статус: новая, в работе, закрыта')

    result = forms.CharField(max_length=20,initial='груз не готов',
                              label='статус2: прошли по цене, груз не готов, не прошли по цене')

