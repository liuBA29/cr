from django.db.models import *
from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from django.urls import resolve
from django.core.files.storage import FileSystemStorage
from django.contrib import messages

from .forms import *
from .models import  *


supplyers_in_sdelka = [
    {'title': 'Перевозчик 1', 'supplyer': 'supplyer_1', 'price': 'sup_price_1', 'currency': 'currency1'},
    {'title': 'Перевозчик 2', 'supplyer': 'supplyer_2', 'price': 'sup_price_2', 'currency': 'currency2'},
    {'title': 'Перевозчик 3', 'supplyer': 'supplyer_3', 'price': 'sup_price_3', 'currency': 'currency3'},
    {'title': 'Перевозчик 4', 'supplyer': 'supplyer_4', 'price': 'sup_price_4', 'currency': 'currency4'},
    {'title': 'Перевозчик 5', 'supplyer': 'supplyer_5', 'price': 'sup_price_5', 'currency': 'currency5'},
    {'title': 'Перевозчик 6', 'supplyer': 'supplyer_6', 'price': 'sup_price_6', 'currency': 'currency6'},
    {'title': 'Перевозчик 7', 'supplyer': 'supplyer_7', 'price': 'sup_price_7', 'currency': 'currency7'},
    {'title': 'Перевозчик 8', 'supplyer': 'supplyer_8', 'price': 'sup_price_8', 'currency': 'currency8'},
    {'title': 'Перевозчик 9', 'supplyer': 'supplyer_9', 'price': 'sup_price_9', 'currency': 'currency9'},
    {'title': 'Перевозчик 10', 'supplyer': 'supplyer_10', 'price': 'sup_price_10', 'currency': 'currency10'},
]

operationss = [
    {'title': 'Котировки', 'key': 'Quotation.objects.all()', 'url_name': 'quotations'},
    {'title': 'Сделки', 'key': 'Sdelka.objects.all()', 'url_name': 'sdelki'},
]


contragentss = [
    {'title': 'Заказчики', 'key': 'Client.objects.all()', 'url_name': 'clients'},
    {'title': 'Перевозчики', 'key': 'Supplyer.objects.all()', 'url_name': 'supplyers'},
    {'title': 'Сторонние компании', 'key': 'OtherCompany.objects.all()', 'url_name': 'other_companies'},
]

docs = [
    {'title': 'Документы Заказчика', 'key': 'Client.objects.all()', 'url_name': 'client_docs'},
    {'title': 'Документы Перевозчика', 'key': 'Supplyer.objects.all()', 'url_name': 'supplyer_docs'},
    {'title': 'Документы Сторонних компаний', 'key': 'OtherCompany.objects.all()', 'url_name': 'other_companies_docs'},
    {'title': 'Корпоративные Документы', 'key': 'OtherCompany.objects.all()', 'url_name': 'corporative_docs'},
]

menu = [
    {'title': 'Контрагенты', 'url_name': 'contragents'},
    {'title': 'Операции', 'url_name': 'operations'},
    {'title': 'Документы', 'url_name': 'documents'},
    {'title': 'Войти', 'url_name': 'login'},
       ]





def index(request):


    return render(request, 'crm_app/index.html', {'menu': menu, "title": "Главная"})


def contragents(request):
    url = resolve(request.path_info).url_name
    sdelka=Sdelka.objects.all()
    alena = Client.objects.filter(contact_name__contains='алена')
    ale = Client.objects.filter(contact_name__icontains='алЕ') #DOESNOT WORK WITH SQL
    perevozchiki = Supplyer.objects.filter(pk__in=[1, 2, 3], supplyer_status=True)
    class_q = Supplyer.objects.filter(Q(pk__in=[1, 2, 3]) | Q(supplyer_status=True))
    q_ne =  Client.objects.filter(~Q(pk__in=[1,2,3]) & ~Q(client_status=True) )
    class_q2 = Supplyer.objects.filter(Q(pk__in=[1, 2, 3]) | Q(pk__in=[5])) #1 importance
    first1 = Supplyer.objects.first()#1st zapis
    in_test = Client.objects.filter(contact_name__in=['алена', 'Вася Пупкин'])
    cur_cl = Sdelka.objects.filter(client_currency__in=[1,2])
    sup_cl = Sdelka.objects.filter(currency1__in=[1, 2])

    context = {
        'url': url,
        'contragentss': contragentss,
        'clients': clients,
        'menu': menu,
        "title": "Конртагенты",
        'alena': alena,
        'ale': ale,
        'class_q': class_q,
        'class_q2': class_q2,
        'perevozchiki': perevozchiki,
        'q_ne': q_ne,
        'first1': first1,
        'in_test': in_test,
        'cur_cl': cur_cl,
        'sup_cl': sup_cl,


    }
    return render(request, 'crm_app/contragents.html', context=context)




def clients(request):
    url = resolve(request.path_info).url_name
    clients = Client.objects.all()
    context = {
        'url': url,
        'contragentss': contragentss,
        'clients': clients,
        'menu': menu,
        "title": "Заказчики",

    }
    return render(request, 'crm_app/clients.html', context=context)

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
    doc_cl = client.documents_set.all()


    clients = Client.objects.all()
    contect = {
        'url': url,
        'contragentss': contragentss,
        'client': client,
        'clients': clients,
        'menu': menu,
        "title": "Заказчик",
        'doc_cl': doc_cl,

    }
    return render(request, 'crm_app/client.html', context=contect)


def show_supplyer(request, c_id):
    supplyer = get_object_or_404(Supplyer, pk=c_id)
    url = resolve(request.path_info).url_name
    doc_cl = supplyer.documents_set.all()

    supplyers = Supplyer.objects.all()
    contect = {
        'url': url,
        'contragentss': contragentss,
        'supplyer': supplyer,
        'supplyers': supplyers,
        'menu': menu,
        "title": "Перевозчик",
        "doc_cl": doc_cl,
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
        "title": "Организация",
    }
    return render(request, 'crm_app/other_company.html', context=contect)

#=========================================
def quot_sdelka(request, c_id):
    sdelka = get_object_or_404(Quotation, pk=c_id)
    quotation = get_object_or_404(Quotation, pk=c_id)
    form = AddSdelkaForm(request.POST or None, instance=quotation)
    url = resolve(request.path_info).url_name
    quotations = Quotation.objects.all()
    context = {
        'form': form,
        'url': url,
        'operationss': operationss,
        'sdelka': sdelka,
        'sdelki': sdelki,
        'quotation': quotation,
        'quotations': quotations,
        'menu': menu,
        "title": "СОЗДАТЬ Сделку из Котировки",
    }
    if form.is_valid():
        form.save()
        messages.success(request, 'Сделка из котировки создана')
        return redirect('sdelki')
    return render(request, 'crm_app/quot_sdelka.html', context=context)




#==============================
# =update_other_company==
def update_other_company(request, c_id):
    other_company = get_object_or_404(OtherCompany, pk=c_id)

    form = AddClientForm(request.POST or None, instance=other_company)
    url = resolve(request.path_info).url_name
    other_companies = OtherCompany.objects.all()
    context = {
        'form': form,
        'url': url,
        'operationss': operationss,
        'other_company': other_company,
        'other_companies': other_companies,

        'menu': menu,
        "title": "Редактировать Организацию",
    }
    if form.is_valid():
        form.save()
        messages.success(request, 'Организация изменена успешно')
        return redirect('other_companies')
    return render(request, 'crm_app/update_other_company.html', context=context)




# ===update_supplyer======
def update_supplyer(request, c_id):
    supplyer = get_object_or_404(Supplyer, pk=c_id)

    form = AddClientForm(request.POST or None, instance=supplyer)
    url = resolve(request.path_info).url_name
    supplyers = Supplyer.objects.all()
    context = {
        'form': form,
        'url': url,
        'operationss': operationss,
        'supplyer': supplyer,
        'supplyers': supplyers,

        'menu': menu,
        "title": "Редактировать Перевозчика",
    }
    if form.is_valid():
        form.save()
        messages.success(request, 'Перевозчик изменен успешно')
        return redirect('supplyers')
    return render(request, 'crm_app/update_supplyer.html', context=context)


# =====update_client ================

def update_client(request, c_id):
    client = get_object_or_404(Client, pk=c_id)

    form = AddClientForm(request.POST or None, instance=client)
    url = resolve(request.path_info).url_name
    clients = Client.objects.all()
    context = {
        'form': form,
        'url': url,
        'operationss': operationss,
        'client': client,
        'clients': clients,

        'menu': menu,
        "title": "Редактировать Заказчика",
    }
    if form.is_valid():
        form.save()
        messages.success(request, 'Заказчик изменен успешно')
        return redirect('clients')
    return render(request, 'crm_app/update_client.html', context=context)


# ===================================

def update_sdelka(request, c_id):
    sdelka = get_object_or_404(Sdelka, pk=c_id)

    form = AddSdelkaForm(request.POST or None, instance=sdelka)
    url = resolve(request.path_info).url_name
    quotations = Sdelka.objects.all()
    context = {
        'form': form,
        'url': url,
        'operationss': operationss,
        'sdelka': sdelka,
        'sdelki': sdelki,

        'menu': menu,
        "title": "Редактировать Сделку",
    }
    if form.is_valid():
        form.save()
        messages.success(request, 'Сделка изменена успешно')
        return redirect('sdelki')
    return render(request, 'crm_app/update_sdelka.html', context=context)
# ====UPDATE QUOTATION



def update_quotation(request, c_id):
    quotation = get_object_or_404(Quotation, pk=c_id)
    form = AddQuotForm(request.POST or None, instance=quotation)
    url = resolve(request.path_info).url_name
    quotations = Quotation.objects.all()
    context = {
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
    return render(request, 'crm_app/update_quotation.html', context=context)


#===================================

def delete_client(request, c_id):
    client = get_object_or_404(Client, pk=c_id)

    if request.method == "POST":
        # confirming delete
        client.delete()
        messages.success(request, 'Заказчик удален успешно')
        return redirect('clients')
    context = {
        'client': client,
        'menu': menu,
        "title": "Удалить заказчика",
    }
    return render(request, 'crm_app/delete_client.html', context=context)

def delete_supplyer(request, c_id):
    supplyer = get_object_or_404(Supplyer, pk=c_id)

    if request.method == "POST":
        # confirming delete
        supplyer.delete()
        messages.success(request, 'Перевозчик удален успешно')
        return redirect('supplyers')
    context = {
        'supplyer': supplyer,
        'menu': menu,
        "title": "Удалить перевозчика",
    }
    return render(request, 'crm_app/delete_supplyer.html', context=context)


def delete_other_company(request, c_id):
    other_company = get_object_or_404(OtherCompany, pk=c_id)

    if request.method == "POST":
        # confirming delete
        other_company.delete()
        messages.success(request, 'Организация удалена успешно')
        return redirect('other_companies')
    context = {
        'other_company': other_company,
        'menu': menu,
        "title": "Удалить организацию",
    }
    return render(request, 'crm_app/delete_other_company.html', context=context)


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

    if request.method == "POST":
        # confirming delete
        sdelka.delete()
        messages.success(request, 'Сделка удалена успешно')
        return redirect('sdelki')
    context = {
        'sdelka': sdelka,
        'menu': menu,
        "title": "Удалить сделку",
    }
    return render(request, 'crm_app/delete_sdelka.html', context=context)


#========================================================================

def show_sdelka(request, c_id):
    sdelka = get_object_or_404(Sdelka, pk=c_id)

    url = resolve(request.path_info).url_name
    sdelki = Sdelka.objects.all()

        #~Q(currency1=2) | ~Q(cusdelkarrency1=2) | ~Q(currency1=2) | ~Q(currency1=2) | ~Q(currency1=2) | ~Q(currency1=2) |)

    context = {
        'url': url,
        'operationss': operationss,
        'sdelka': sdelka,
        'sdelki': sdelki,
        'menu': menu,
        "title": f'Сделка № {str(sdelka.number)}',


    }
    return render(request, 'crm_app/sdelka.html', context=context)



def show_quotation(request, c_id):
    quotation = get_object_or_404(Quotation, pk=c_id)
    url = resolve(request.path_info).url_name
    proshli_po_cene = Quotation.objects.filter(status="PRICE_GOOD")

    quotations = Quotation.objects.all()
    contect = {
        'url': url,
        'operationss': operationss,
        'quotation': quotation,
        'quotations': quotations,
        'menu': menu,
        'proshli_po_cene': proshli_po_cene,
        "title": "Котировка",

    }
    return render(request, 'crm_app/quotation.html', context=contect)

# operations==========


def operations(request):
    euro = Currency.objects.get(pk=2)
    sdelka = Sdelka.objects.get(pk=3)
    sdelki = Sdelka.objects.all()
    euro_insdelka = euro.client_currency.all()
    euro_insdelka_count = euro.client_currency.count()
    late_d = Sdelka.objects.latest('time_update')
    next_d = late_d.get_previous_by_time_update()  # this isprevious get_next_by will be next
    next_d_by = late_d.get_previous_by_time_update(client_currency=2)
    is_supl_2 = Sdelka.objects.filter(supplyer_3=4)
    agr_f= Sdelka.objects.aggregate(Max('client_currency'))
    agr_f2 = Sdelka.objects.aggregate(Max('client_currency'), Min('client_currency'))
    valu = Sdelka.objects.values('supplyer_1', 'supplyer_2', 'supplyer_3', 'supplyer_4', 'supplyer_5', 'supplyer_6',).filter(pk__gt=2)
    efe= Sdelka.objects.filter(client_currency__gt=F('currency1')) #сумма клиента больше ілі = суммы перевозчика

    context = {
        'operationss': operationss,
        'quotations': quotations,
        'menu': menu,
        "title": "Операции",
        'euro': euro,
        'euro_insdelka': euro_insdelka,
        'supplyers_in_sdelka': supplyers_in_sdelka,
        'sdelka': sdelka,
        'sdelki': sdelki,
        'late_d': late_d,
        'next_d': next_d,
        'next_d_by': next_d_by,
        'is_supl_2': is_supl_2,
        'agr_f': agr_f,
        'agr_f2': agr_f2,
        'valu': valu,
        'efe': efe,
    }
    return render(request, 'crm_app/operations.html', context=context)

#========================




def quotations(request):
    quotations = Quotation.objects.all()

    context = {
        'operationss': operationss,
        'quotations': quotations,
        'menu': menu,
        "title": "Котировки",
    }
    return render(request, 'crm_app/quotations.html', context=context)


def sdelki(request):
    sdelki = Sdelka.objects.all()
    euro = Currency.objects.get(id=2)

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
            messages.success(request, f'Сделка успешно добавлена!')
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
           print(form.cleaned_data)
           messages.success(request, 'Котировка добавлена')
           return redirect('quotations')
    else:
        form = AddQuotForm()
    return render(request, 'crm_app/add_quotation.html',  {'form': form,  'menu': menu, 'title': 'Создать котировку'})


#===documents

def upload_documents(request):
    sdelki = Sdelka.objects.all()
    documents = Documents.objects.all()
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

        context = {
            'form': form,
            'operationss': operationss,
            'sdelki': sdelki,
            'menu': menu,
            'documents': documents,
            "title": "Документы",

        }
    return render(request, 'crm_app/documents.html',  context=context)

#-----------============================------------------

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