from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from django.urls import resolve
from django.core.files.storage import FileSystemStorage
from django.contrib import messages

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
        messages.success(request, 'Котировка изменена успешно')
        return redirect('quotations')
    return render(request, 'crm_app/update_quotation.html', context=contect)


#===================================
# delete quotation:
def delete_quotation(request, c_id):
    quotation = get_object_or_404(Quotation, pk=c_id)

    if request.method == "POST":
        #confirming delete
        quotation.delete()
        messages.success(request, 'Котировка удалена успешно')
        return redirect('quotations')
    context = {
        'quotation': quotation,
        'menu': menu,
        "title": "Удалить котировку",
    }
    return render(request, 'crm_app/delete_quotation.html', context=context)


def delete_sdelka(request, c_id):
    sdelka = get_object_or_404(Sdelka, pk=c_id)
    sdelka.delete()
    messages.success(request, 'Сделка удалена успешно')
    return redirect('sdelki')


#========================================================================

def show_sdelka(request, c_id):
    sdelka = get_object_or_404(Sdelka, pk=c_id)
    url = resolve(request.path_info).url_name
    sdelki = Sdelka.objects.all()
    context = {
        'url': url,
        'operationss': operationss,
        'sdelka': sdelka,
        'sdelki': sdelki,
        'menu': menu,
        "title": "Сделка",
    }
    return render(request, 'crm_app/sdelka.html', context=context)



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

    if request.method == "POST":
        form = AddSdelkaForm(request.POST, request.FILES)
        if form.is_valid():
            # print(form.cleaned_data)
            form.save()
            messages.success(request, 'Сделка добавлена')
            return redirect('sdelki')
    else:
        form = AddSdelkaForm()

    return render(request, 'crm_app/add_sdelka.html',  { 'form': form, 'menu': menu, 'title': 'Создать сделку'})


def add_client(request):
    if request.method == 'POST':
        form = AddClientForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Заказчик добавлен')
            return redirect('clients')
    else:
        form = AddClientForm()
    return render(request, 'crm_app/add_client.html', {'form': form,  'menu': menu, 'title': 'Создать Заказчика'})



def add_supplyer(request):
    if request.method == 'POST':
        form = AddSupplyerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('supplyers')
    else:
        form = AddSupplyerForm()
        messages.success(request, 'Перевозчик добавлен')
    return render(request, 'crm_app/add_supplyer.html', {'form': form,  'menu': menu, 'title': 'Создать Перевозчика'})

def add_othercompany(request):
    if request.method == 'POST':
        form = AddOtherCompanyForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Организация добавлена')
            return redirect('other_companies')
    else:
        form = AddOtherCompanyForm()
    return render(request, 'crm_app/add_othercompany.html', {'form': form,  'menu': menu, 'title': 'Создать Стороннюю Организацию'})

#================================




def add_quotation(request):
    if request.method == "POST":
        form = AddQuotForm(request.POST)
        if form.is_valid():
           form.save()
           messages.success(request, 'Котировка добавлена')
           return redirect('quotations')
    else:
        form = AddQuotForm()
    return render(request, 'crm_app/add_quotation.html',  {'form': form,  'menu': menu, 'title': 'Создать котировку'})




def upload_documents(request):
    if request.method == 'POST':
        form = UploadDocumentsForm(request.POST, request.FILES)
        #file = request.FILES.getlist('file')[1]
        file = request.FILES['file']
        client = Client.objects.get(pk=1)
        supplyer1 = Supplyer.objects.get(pk=1)
        print(client)
        print(supplyer1)
        client_document=Sdelka.objects.create(client=client, supplyer1=supplyer1, cl_documents=file)
        client_document.save()
        return HttpResponse('file added to sdelka: ' + str(client_document.pk))
    else:
        form = UploadDocumentsForm()

    return render(request, 'crm_app/documents.html',  { 'form': form, 'menu': menu, 'title': 'Документы'})



def sdelka_vypiska(request):


    '''простые запросы'''
    value = ""
    '''
    & - і (пріор 2)
    | - ілі (пріор 3)
    ~ - не (пріор 1)
    
    __gt  >
    __gte >=
    __lt  <
    __lte <=
    '''
    obj_list = Sdelka.objects.filter(client=1).all()
    return render(request, 'crm_app/extract.html', {'obj_list': obj_list, 'value': value} )