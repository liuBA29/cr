from django.shortcuts import render, HttpResponse
from .forms import *
from .models import  *


menu =[

    {'title': 'Контрагенты', 'url_name': 'contragents'},
    {'title': 'Операции', 'url_name': 'operations'},
    {'title': 'Войти', 'url_name': 'login'},
       ]

def index(request):
    return render(request, 'crm_app/index.html', {'menu': menu, "title": "Главная"})


def contragents(request):
    return render(request, 'crm_app/contragents.html', {'menu': menu, "title": "Контрагенты"})

def operations(request):
    return render(request, 'crm_app/operations.html', {'menu': menu, "title": "Операции"})

def login(request):
    return render(request, 'crm_app/login.html', {'menu': menu, "title": "Войти"})



#=============Forms add+++++++++++++++++
def add_sdelka(request):
    if request.method == 'POST':
        form = SdelkaForm(request.POST)

        if form.is_valid():
            print(form.cleaned_data)

    else:
        form = SdelkaForm()
    return render(request, 'crm_app/add_sdelka.html',  {'form':form,  'menu': menu, 'title': 'Создать cltkre'})


def add_stavka(request):
    if request.method == 'POST':
        form = StavkaForm(request.POST)

        if form.is_valid():
            print(form.cleaned_data)

    else:
        form = StavkaForm()
    return render(request, 'crm_app/add_sdelka.html',  {'form':form,  'menu': menu, 'title': 'добавітьe'})
