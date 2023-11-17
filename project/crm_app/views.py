from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from django.urls import resolve

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
    url = resolve(request.path_info).url_name
    return render(request, 'crm_app/contragents.html', {'url':url,  'contragentss': contragentss, 'menu': menu, "title": "Контрагенты"})




def clients(request):
    url = resolve(request.path_info).url_name
    clients = Client.objects.all()
    contect = {
        'url': url,
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


def show_client(request, c_id):
    client = get_object_or_404(Client, pk=c_id)
    url = resolve(request.path_info).url_name

    clients = Client.objects.all()
    contect = {
        'url': url,
        'contragentss': contragentss,
        'client': client,
        'clients': clients,
        'menu': menu,
        "title": "Заказчики",
    }
    return render(request, 'crm_app/client.html', context=contect)


def show_supplyer(request, c_id):
    supplyer = get_object_or_404(Supplyer, pk=c_id)
    url = resolve(request.path_info).url_name

    supplyers = Supplyer.objects.all()
    contect = {
        'url': url,
        'contragentss': contragentss,
        'supplyer': supplyer,
        'supplyers': supplyers,
        'menu': menu,
        "title": "Перевозчики",
    }
    return render(request, 'crm_app/supplyer.html', context=contect)


def show_other_company(request, c_id):
    other_company = get_object_or_404(OtherCompany, pk=c_id)
    url = resolve(request.path_info).url_name

    other_companys = OtherCompany.objects.all()
    contect = {
        'url': url,
        'contragentss': contragentss,
        'other_company': other_company,
        'other_companys': other_companys,
        'menu': menu,
        "title": "Перевозчики",
    }
    return render(request, 'crm_app/other_company.html', context=contect)



def update_quotation(request, c_id):
    quotation = get_object_or_404(Quotation, pk=c_id)
    form = AddQuotForm(request.POST or None, instance=quotation)
    url = resolve(request.path_info).url_name
    quotations = Quotation.objects.all()
    contect = {
        'form': form,
        'url': url,
        'operationss': operationss,
        'quotation': quotation,
        'quotations': quotations,
        'menu': menu,
        "title": "Редактировать Котировку",
    }
    if form.is_valid():
        form.save()
        return redirect('quotations')
    return render(request, 'crm_app/update_quotation.html', context=contect)

#delete quotation:
def delete_quotation(request, c_id):
    quotation = get_object_or_404(Quotation, pk=c_id)
    quotation.delete()
    return redirect('quotations')



def show_quotation(request, c_id):
    quotation = get_object_or_404(Quotation, pk=c_id)
    url = resolve(request.path_info).url_name

    quotations = Quotation.objects.all()
    contect = {
        'url': url,
        'operationss': operationss,
        'quotation': quotation,
        'quotations': quotations,
        'menu': menu,
        "title": "Котировка",
    }
    return render(request, 'crm_app/quotation.html', context=contect)


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
    return render(request, 'crm_app/add_sdelka.html',  { 'menu': menu, 'title': 'Создать cltkre'})



def add_quotation(request):

    if request.method == "POST":
        form = AddQuotForm(request.POST)
        if form.is_valid():
            #print(form.cleaned_data)
            try:
                Quotation.objects.create(**form.cleaned_data)
                return redirect('quotations')
            except:
                form.add_error(None, 'ошибка добавления котировки')
    else:
        form = AddQuotForm()
    return render(request, 'crm_app/add_quotation.html',  {'form': form, 'menu': menu, 'title': 'Создать котировку'})


