from django.shortcuts import render, HttpResponse
from .forms import *
from .models import  *

operationss = [
    {'title': 'Котировки', 'key': 'Quotation.objects.all()', 'url_name': 'quotations'},
    {'title': 'Сделки', 'key': 'Sdelka.objects.all()', 'url_name': 'sdelki'},
]


contragentss = [
    {'title': 'Заказчики', 'key': 'Client.objects.all()', 'url_name': 'clients'},
    {'title': 'Перевозчики', 'key': 'Supplyer.objects.all()', 'url_name': 'supplyers'},
    {'title': 'Сторонние компании', 'key': 'OtherCompany.objects.all()', 'url_name': 'other_companies'},
]

menu =[
    {'title': 'Контрагенты', 'url_name': 'contragents'},
    {'title': 'Операции', 'url_name': 'operations'},
    {'title': 'Войти', 'url_name': 'login'},
       ]

def index(request):
    return render(request, 'crm_app/index.html', {'menu': menu, "title": "Главная"})


def contragents(request):
    return render(request, 'crm_app/contragents.html', {'contragentss': contragentss, 'menu': menu, "title": "Контрагенты"})


def clients(request):
    clients = Client.objects.all()
    contect = {
        'contragentss': contragentss,
        'clients': clients,
        'menu': menu,
        "title": "Заказчики",
    }
    return render(request, 'crm_app/clients.html', context=contect)

def supplyers(request):
    supplyers = Supplyer.objects.all()
    contect = {
        'contragentss': contragentss,
        'supplyers': supplyers,
        'menu': menu,
        "title": "Перевозчики",
    }
    return render(request, 'crm_app/supplyers.html', context=contect)

def other_companies(request):
    other_companies = OtherCompany.objects.all()
    contect = {
        'contragentss': contragentss,
        'other_companies': other_companies,
        'menu': menu,
        "title": "Другие организации",
    }
    return render(request, 'crm_app/other_companies.html', context=contect)


def show_contragent(request, c_id):
    return HttpResponse(f'reflexing contr with id = {c_id}')


def show_operation(request, c_id):
    return HttpResponse(f'reflexing operation with id = {c_id}')


def operations(request):
    return render(request, 'crm_app/operations.html',
                  {'operationss': operationss, 'menu': menu, "title": "Операции"})

def quotations(request):
    quotations = Quotation.objects.all()
    contect = {
        'operationss': operationss,
        'quotations': quotations,
        'menu': menu,
        "title": "Котировки",
    }
    return render(request, 'crm_app/quotations.html', context=contect)


def sdelki(request):
    sdelki = Sdelka.objects.all()
    contect = {
        'operationss': operationss,
        'sdelki': sdelki,
        'menu': menu,
        "title": "Сделки",
    }
    return render(request, 'crm_app/sdelki.html', context=contect)



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
