import calendar
from calendar import HTMLCalendar
from pprint import pprint
import csv
from django.db.models import *
from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from django.urls import resolve
from django.core.files.storage import FileSystemStorage
from django.contrib import messages
from django.views.generic import ListView
from dateutil.relativedelta import relativedelta
from .forms import *
from .models import *
from django.http import HttpResponse
from datetime import datetime, timedelta, date
from dateutil.relativedelta import relativedelta
from django.db.models.functions import *

#============= declare now_time ++++++++++=========
now = datetime.now()
now_year = now.year
# ================functions===============
def period_quartal():
    '''считаем период за квартал'''
    m1, m2, m3 = 0, 0, 0

    period = datetime.now() - timedelta(days=30)
    # period.month  period.year
    m = datetime(period.year, period.month, day=12)
    '''дней первого месяца ...'''
    m1 = m + relativedelta(day=31)
    m1 = m1.day
    period = period - timedelta(days=m1)
    m = datetime(period.year, period.month, day=12)
    m2 = m + relativedelta(day=31)
    m2 = m2.day
    period = period - timedelta(days=m2)
    m = datetime(period.year, period.month, day=12)
    m3 = m + relativedelta(day=31)
    m3 = m3.day
    result = datetime.now() - timedelta(days=m1 + m2 + m3)
    print(result)
    return result


def six_months_period():
    '''считаем период за 6 месяцев'''
    m1, m2, m3, m4, m5, m6 = 0, 0, 0, 0, 0, 0

    period = datetime.now() - timedelta(days=30)
    # period.month  period.year
    m = datetime(period.year, period.month, day=12)
    '''дней первого месяца ...'''
    m1 = m + relativedelta(day=31)
    m1 = m1.day
    period = period - timedelta(days=m1)
    m = datetime(period.year, period.month, day=12)
    m2 = m + relativedelta(day=31)
    m2 = m2.day
    period = period - timedelta(days=m2)
    m = datetime(period.year, period.month, day=12)
    m3 = m + relativedelta(day=31)
    m3 = m3.day
    period = period - timedelta(days=m3)
    m = datetime(period.year, period.month, day=12)
    m4 = m + relativedelta(day=31)
    m4 = m4.day
    period = period - timedelta(days=m4)
    m = datetime(period.year, period.month, day=12)
    m5 = m + relativedelta(day=31)
    m5 = m5.day
    period = period - timedelta(days=m5)
    m = datetime(period.year, period.month, day=12)
    m6 = m + relativedelta(day=31)
    m6 = m6.day
    result = datetime.now() - timedelta(days=m1 + m2 + m3 + m4 + m5 + m6)
    return result


# ============================end function+++++++++++++++++++

selectings = [
    {'selected': 3, 'title': 'period_quartal'},
    {'selected': 6, 'title': 'six_month'},
    {'selected': 1, 'title': 'week'},

]

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

documentss = [
    {'title': 'Документы Заказчиков',  'url_name': 'clients_docs'},
    {'title': 'Документы Перевозчиков', 'url_name': 'supplyers_docs'},
    {'title': 'Другие Документы', 'url_name': 'other_companies_docs'},


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


def index(request, year=datetime.now().year, month=datetime.now().strftime('%B')):
    name = "Calendar"
    month = month.title()
    # convert month from name to number
    month_number = list(calendar.month_name).index(month)
    month_number = int(month_number)
    now = datetime.now()

    now_year = now.year
    time = now.strftime('%H:%M')
    # create calendar
    cal = calendar.HTMLCalendar().formatmonth(
        year,
        month_number)

    # query the search for date
    client_search_month = Client.objects.filter(
        time_create__year=year,
        time_create__month=month_number,

    )
    client_search_year = Client.objects.filter(
        time_create__year=year,
    )

    context = {
        'name': name,
        'menu': menu,
        "title": "Главная",
        "year": year,
        "month": month,
        "month_number": month_number,
        'cal': cal,
        'now_year': now_year,
        'now': now,
        'time': time,
        'client_search_month': client_search_month,
        'client_search_year': client_search_year,

    }

    return render(request, 'crm_app/index.html', context=context)


def contragents(request):
    url = resolve(request.path_info).url_name
    sdelka = Sdelka.objects.all()
    alena = Client.objects.filter(contact_name__contains='алена')
    ale = Client.objects.filter(contact_name__icontains='алЕ')  # DOESNOT WORK WITH SQL
    perevozchiki = Supplyer.objects.filter(pk__in=[1, 2, 3], supplyer_status=True)
    class_q = Supplyer.objects.filter(Q(pk__in=[1, 2, 3]) | Q(supplyer_status=True))
    q_ne = Client.objects.filter(~Q(pk__in=[1, 2, 3]) & ~Q(client_status=True))
    class_q2 = Supplyer.objects.filter(Q(pk__in=[1, 2, 3]) | Q(pk__in=[5]))  # 1 importance
    first1 = Supplyer.objects.first()  # 1st zapis
    in_test = Client.objects.filter(contact_name__in=['алена', 'Вася Пупкин'])
    cur_cl = Sdelka.objects.filter(client_currency__in=[1, 2])
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
        'now_year': now_year,

    }
    return render(request, 'crm_app/contragents.html', context=context)



def clients(request):
    url = resolve(request.path_info).url_name
    clients = Client.objects.all()
    three = period_quartal()
    six = six_months_period()
    now = datetime.now()
    clients_three = clients.filter(time_create__gte=three)
    clients_six = clients.filter(time_create__gte=six)
    context = {
        'now_year': now_year,
        'url': url,
        'contragentss': contragentss,
        'clients': clients,
        'menu': menu,
        "title": "Заказчики",
        'six': six,
        'now': now,
        'clients_six': clients_six,
        'clients_three': clients_three,
        'selectings': selectings,


    }
    return render(request, 'crm_app/clients.html', context=context)


def supplyers(request):
    supplyers = Supplyer.objects.all()
    '''3 month search'''
    three = period_quartal()
    # selected=1

    supplyers_three = supplyers.filter(time_create__gte=three)
    '''6 month search'''
    six = six_months_period()
    now = datetime.now()
    supplyers_six = supplyers.filter(time_create__gte=six)

    context = {
        'now_year': now_year,
        'contragentss': contragentss,
        'supplyers': supplyers,
        'menu': menu,
        "title": "Перевозчики",
        'supplyers_six': supplyers_six,
        'supplyers_three': supplyers_three,
        # 'selected':selected,
        'selectings': selectings,

        'now': now,
    }
    return render(request, 'crm_app/supplyers.html', context=context)


def other_companies(request):
    other_companies = OtherCompany.objects.all()
    context = {
        'now_year': now_year,
        'contragentss': contragentss,
        'other_companies': other_companies,
        'menu': menu,
        "title": "Другие организации",
    }
    return render(request, 'crm_app/other_companies.html', context=context)



#-------------------



def show_client(request, c_id):
    client = get_object_or_404(Client, pk=c_id)
    url = resolve(request.path_info).url_name
    doc_cl = client.documents_set.all()

    clients = Client.objects.all()
    context = {
        'now_year': now_year,
        'url': url,
        'contragentss': contragentss,
        'client': client,
        'clients': clients,
        'menu': menu,
        "title": "Заказчик",
        'doc_cl': doc_cl,

    }
    return render(request, 'crm_app/client.html', context=context)


def show_supplyer(request, c_id):
    supplyer = get_object_or_404(Supplyer, pk=c_id)
    url = resolve(request.path_info).url_name
    doc_cl = supplyer.documents_set.all()

    supplyers = Supplyer.objects.all()
    context = {
        'now_year': now_year,
        'url': url,
        'contragentss': contragentss,
        'supplyer': supplyer,
        'supplyers': supplyers,
        'menu': menu,
        "title": "Перевозчик",
        "doc_cl": doc_cl,
    }
    return render(request, 'crm_app/supplyer.html', context=context)


def show_other_company(request, c_id):
    other_company = get_object_or_404(OtherCompany, pk=c_id)
    url = resolve(request.path_info).url_name

    other_companys = OtherCompany.objects.all()
    context = {
        'now_year': now_year,
        'url': url,
        'contragentss': contragentss,
        'other_company': other_company,
        'other_companys': other_companys,
        'menu': menu,
        "title": "Организация",
    }
    return render(request, 'crm_app/other_company.html', context=context)





# ==============================
# =update_other_company==
def update_other_company(request, c_id):
    other_company = get_object_or_404(OtherCompany, pk=c_id)

    form = AddClientForm(request.POST or None, instance=other_company)
    url = resolve(request.path_info).url_name
    other_companies = OtherCompany.objects.all()
    context = {
        'now_year': now_year,
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

    form = AddSupplyerForm(request.POST or None, instance=supplyer)
    url = resolve(request.path_info).url_name
    supplyers = Supplyer.objects.all()
    context = {
        'now_year': now_year,
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
        'now_year': now_year,
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
        'now_year': now_year,
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
        'now_year': now_year,
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


# ===================================

def delete_client(request, c_id):
    client = get_object_or_404(Client, pk=c_id)
    if request.method == "POST":
        # confirming delete
        client.delete()
        messages.success(request, 'Заказчик удален успешно')
        return redirect('clients')
    context = {
        'now_year': now_year,
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
        'now_year': now_year,
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
        'now_year': now_year,
        'other_company': other_company,
        'menu': menu,
        "title": "Удалить организацию",
    }
    return render(request, 'crm_app/delete_other_company.html', context=context)


# delete quotation:
def delete_quotation(request, c_id):
    quotation = get_object_or_404(Quotation, pk=c_id)

    if request.method == "POST":
        # confirming delete
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
        'now_year': now_year,
        'sdelka': sdelka,
        'menu': menu,
        "title": "Удалить сделку",
    }
    return render(request, 'crm_app/delete_sdelka.html', context=context)
#=================delete document====================
def delete_document(request, c_id):
    document = get_object_or_404(Documents, pk=c_id)
    if request.method == "POST":
        # confirming delete
        document.delete()
        messages.success(request, 'Документ удален успешно')
        return redirect('documents')
    context = {
        'now_year': now_year,
        'document': document,
        'menu': menu,
        "title": "Удалить документ",
    }
    return render(request, 'crm_app/delete_document.html', context=context)





# =======SEARCHING, FILTERRING, ETC========
class ClassicSearchSupplyer(ListView):
    model = Supplyer
    context_object_name = 'supplyers'
    now = datetime.now()
    now_year = now.year
    def get_queryset(self):
        return Supplyer.objects.filter(company_name__iregex=self.request.GET.get('q'))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now_year']: now_year
        context['title'] = 'Поиск Перевозчика(-иков)'
        context['menu'] = menu
        context['contragentss'] = contragentss
        context['q'] = self.request.GET.get('q')
        return context


class ClassicSearchClient(ListView):
    model = Client
    context_object_name = 'clients'

    def get_queryset(self):
        return Client.objects.filter(company_name__iregex=self.request.GET.get('q'))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now_year']: now_year
        context['title'] = 'Поиск Заказчика(-иков)'
        context['menu'] = menu
        context['contragentss'] = contragentss
        context['q'] = self.request.GET.get('q')
        return context


class ClassicSearchQuotation(ListView):
    model = Quotation
    context_object_name = 'quotations'

    def get_queryset(self):
        return Quotation.objects.filter(description__iregex=self.request.GET.get('q'))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Поиск Котировки(-вок)'
        context['menu'] = menu
        context['operationss'] = operationss
        context['q'] = self.request.GET.get('q')
        return context


class ClassicSearchSdelka(ListView):
    model = Sdelka
    context_object_name = 'sdelki'

    def get_queryset(self):
        return Sdelka.objects.filter(description__iregex=self.request.GET.get('q'))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Поиск Сделки(-ок)'
        context['menu'] = menu
        context['operationss'] = operationss
        context['q'] = self.request.GET.get('q')
        return context

''' Сортііровка по неделе, кварталу, 6 месяцам, все....'''
#==========
#========show document==========
def show_document(request, c_id):
    document = get_object_or_404(Documents, pk=c_id)
    url = resolve(request.path_info).url_name
    context={
        'document': document,
        'url': url,
        'now_year': now_year,
        'url': url,
        'documentss': documentss,
        'menu': menu,
        "title": "Документ",
    }
    return render(request, 'crm_app/document.html', context=context)
#==================================================================
def clients_docs(request):
    sdelki = Sdelka.objects.all()
    documents = Documents.objects.all()
    dogovory = Documents.objects.filter(type='Договор')
    '''for choosing clients files'''
    documents = Documents.objects.annotate(len=Length('client'))
    context = {
        'now_year': now_year,
        'sdelki': sdelki,
        'menu': menu,
        'documents': documents,
        'documentss': documentss,
        "title": "Документы Заказчиков",

        'dogovory': dogovory,
        'clients_docs': clients_docs,
    }
    return render(request, 'crm_app/clients_docs.html', context=context)
#=====

def docs_types_other_companies(request, pk):
    documents= Documents.objects.all()
    documents = Documents.objects.annotate(len=Length('other_company'))
    title2 = ''
    if pk == 5:
        documents = documents.filter(type='Корпоративные')
        title2 = 'Корпоративные'
    elif pk == 6:
        documents = Documents.objects.annotate(len=Length('other_company'))
        title2 = 'Другие'
    context = {
        'documentss': documentss,
        'now_year': now_year,
        'documents': documents,
        "title": "Документы другие",
        'title2': title2,
        'menu': menu,
        }
    return render(request, 'crm_app/clients_docs.html', context=context)
# ====

# ====
def docs_types_supplyers(request, pk):
    documents= Documents.objects.all()
    documents = Documents.objects.annotate(len=Length('supplyer'))
    title2 = ''
    if pk == 1:
        documents = documents.filter(type='Договор')
        title2 = 'Договоры'
    elif pk == 2:
        documents = documents.filter(type='Коносамент')
        title2 = 'Коносаменты'
    elif pk == 3:
        documents = documents.filter(type='ТН')
        title2 = 'ТН'
    elif pk == 4:
        documents = documents.filter(type='Дебиторка')
        title2 = 'Дебиторки'
    elif pk == 5:
        documents = documents.filter(type='Корпоративные')
    context = {
        'documentss': documentss,
        'now_year': now_year,
        'documents': documents,
        "title": "Документы Перевозчиков",
        'title2': title2,
        'menu': menu,
        }
    return render(request, 'crm_app/clients_docs.html', context=context)
# ====
def docs_types(request, pk):
    documents= Documents.objects.all()
    documents = Documents.objects.annotate(len=Length('client'))
    title2 = ''
    if pk == 1:
        documents = documents.filter(type='Договор')
        title2 = 'Договоры'
    elif pk == 2:
        documents = documents.filter(type='Коносамент')
        title2 = 'Коносаменты'
    elif pk == 3:
        documents = documents.filter(type='ТН')
        title2 = 'ТН'
    elif pk == 4:
        documents = documents.filter(type='Дебиторка')
        title2 = 'Дебиторки'
    elif pk == 5:
        documents = documents.filter(type='Корпоративные')
    context = {
        'documentss': documentss,
        'now_year': now_year,
        'documents': documents,
        "title": "Документы Заказчиков",
        'title2': title2,
        'menu': menu,
        }
    return render(request, 'crm_app/clients_docs.html', context=context)

##========================supplyers_filter========
def supplyers_filter(request, pk):
    supplyers = Supplyer.objects.all()
    title2 = f'C _____ по настоящее время:'
    now_str = datetime.now().strftime("%d.%m.%Y")
    if pk == 1:
        now = datetime.now() - timedelta(minutes=60 * 24 * 7)  # 60*24---это сутки*7  =неделя
        supplyers = supplyers.filter(time_create__gte=now)
        selected = 1
    elif pk == 2:
        now = datetime.now()
        supplyers = Supplyer.objects.all()
        selected = True
    elif pk == 3:
        '''3 month search'''
        three = period_quartal()
        now = datetime.now()
        supplyers = supplyers.filter(time_create__gte=three)
        selected = 3
    elif pk == 6:
        '''6 month search'''
        six = six_months_period()
        now = datetime.now()
        supplyers = supplyers.filter(time_create__gte=six)
        selected = 6
    context = {
        'now_year': now_year,
        'supplyers': supplyers,
        'menu': menu,
        "title": " Перевозчики за период: ",
        'selected': selected,
        'selectings': selectings,
        'now': now,
        'now_str': now_str,
        'operationss': operationss,
        'contragentss': contragentss,
    }
    return render(request, 'crm_app/supplyers.html', context=context)


##=================== clients  filter=================
def clients_filter(request, pk):

    supplyers = Supplyer.objects.all()
    clients = Client.objects.all()
    title2 = f'C _____ по настоящее время:'
    now_str = datetime.now().strftime("%d.%m.%Y")
    if pk == 1:
        now = datetime.now() - timedelta(minutes=60 * 24 * 7)  # 60*24---это сутки*7  =неделя
        clients = clients.filter(time_create__gte=now)
        selected = 1
    elif pk == 2:
        now = datetime.now()
        clients = Client.objects.all()
        selected = True
    elif pk == 3:
        '''3 month search'''
        three = period_quartal()
        now = datetime.now()
        clients = clients.filter(time_create__gte=three)
        selected = 3
    elif pk == 6:
        '''6 month search'''
        six = six_months_period()
        now = datetime.now()
        clients = clients.filter(time_create__gte=six)
        selected = 6
    context = {
        'now_year': now_year,
        'clients': clients,
        'menu': menu,
        "title": "Заказчики за период: ",
        'selected': selected,
        'selectings': selectings,
        'now': now,
        'now_str': now_str,
        'operationss': operationss,
        'contragentss': contragentss,
        'supplyers': supplyers,
    }
    return render(request, 'crm_app/clients.html', context=context)

def quotations_filter(request, pk):
    quotations = Quotation.objects.all()
    title2 = f'C _____ по настоящее время:'
    now_str = datetime.now().strftime("%d.%m.%Y")
    if pk == 1:
        now = datetime.now() - timedelta(minutes=60 * 24 * 7)  # 60*24---это сутки*7  =неделя
        quotations = quotations.filter(time_create__gte=now)
        selected = 1
    elif pk == 2:
        now = datetime.now()
        quotations = Quotation.objects.all()
        selected = True
    elif pk == 3:
        '''3 month search'''
        three = period_quartal()
        now = datetime.now()
        quotations = quotations.filter(time_create__gte=three)
        selected = 3
    elif pk == 6:
        '''6 month search'''
        six = six_months_period()
        now = datetime.now()
        quotations = quotations.filter(time_create__gte=six)
        selected = 6
    context = {
        'now_year': now_year,
        'quotations': quotations,
        'menu': menu,
        "title": " Котировки за период: ",
        'selected': selected,
        'selectings': selectings,
        'now': now,
        'now_str': now_str,
        'operationss': operationss,
        'contragentss': contragentss,
    }
    return render(request, 'crm_app/quotations.html', context=context)

#-----------------------------------------
def sdelki_filter(request, pk):
    sdelki = Sdelka.objects.all()
    title2 = f'C _____ по настоящее время:'
    now_str = datetime.now().strftime("%d.%m.%Y")
    if pk == 1:
        now = datetime.now() - timedelta(minutes=60 * 24 * 7)  # 60*24---это сутки*7  =неделя
        sdelki = sdelki.filter(time_create__gte=now)
        selected = 1
    elif pk == 2:
        now = datetime.now()
        sdelki = sdelki.objects.all()
        selected = True
    elif pk == 3:
        '''3 month search'''
        three = period_quartal()
        now = datetime.now()
        sdelki = sdelki.filter(time_create__gte=three)
        selected = 3
    elif pk == 6:
        '''6 month search'''
        six = six_months_period()
        now = datetime.now()
        sdelki = sdelki.filter(time_create__gte=six)
        selected = 6
    context = {
        'now_year': now_year,
        'sdelki': sdelki,
        'menu': menu,
        "title": " Сделки за период: ",
        'selected': selected,
        'selectings': selectings,
        'now': now,
        'now_str': now_str,
        'operationss': operationss,
        'contragentss': contragentss,
    }
    return render(request, 'crm_app/sdelki.html', context=context)


# =========supplyers_for_period=====
def supplyers_for_period(request):
    supplyers = Supplyer.objects.all()
    if request.method == "POST":
        fromdate = request.POST.get('fromdate')
        todate = request.POST.get('todate')
        day = timedelta(minutes=60 * 24)
        end_date = datetime.today() + timedelta(days=1)
        typed = type(day)
        end_date2 = end_date.strftime("%Y-%m-%d")
        typedd = type(todate)

        # result = Supplyer.objects.filter(time_create__lte=todate, time_create__gte=fromdate)
        result = Supplyer.objects.raw(
            'select * from crm_app_supplyer where time_create between "' + fromdate + '" and "' + todate + '"')

    else:
        result = "Что-то пошло не так .. "
    context = {
        'now_year': now_year,
        'fromdate': fromdate,
        'todate': todate,
        'contragentss': contragentss,
        'supplyers': supplyers,
        'menu': menu,
        "title": "Перевозчики",
        'result': result,
        'day': day,
        'end_date2': end_date2,

        'typed': typed,
        'typedd': typedd,
        'end_date': end_date,
    }
    return render(request, 'crm_app/supplyers_for_period.html', context=context)


# ==========================================================
def clients_for_period(request):
    clients = Client.objects.all()
    if request.method == "POST":
        fromdate = request.POST.get('fromdate')
        todate = request.POST.get('todate')
        day = timedelta(minutes=60 * 24)
        end_date = datetime.today() + timedelta(days=1)
        typed = type(day)
        end_date2 = end_date.strftime("%Y-%m-%d")
        typedd = type(todate)
        clients = Client.objects.raw(
            'select * from crm_app_client where time_create between "' + fromdate + '" and "' + todate + '"')

    else:
        result = "Что-то пошло не так .. "
    context = {
        'now_year': now_year,
        'fromdate': fromdate,
        'todate': todate,
        'contragentss': contragentss,
        'clients': clients,
        'menu': menu,
        "title": "Перевозчики",

        'day': day,
        'end_date2': end_date2,

        'typed': typed,
        'typedd': typedd,
        'end_date': end_date,
    }
    return render(request, 'crm_app/clients_for_period.html', context=context)


# =========================quotation by period==========================
def quotations_for_period(request):
    quotations = Quotation.objects.all()
    if request.method == "POST":
        fromdate = request.POST.get('fromdate')
        todate = request.POST.get('todate')
        day = timedelta(minutes=60 * 24)
        end_date = datetime.today() + timedelta(days=1)
        typed = type(day)
        end_date2 = end_date.strftime("%d.%m.%Y")



        typedd = type(todate)
        result = Quotation.objects.raw(
            'select * from crm_app_quotation where time_create between "' + fromdate + '" and "' + todate + '"')

    else:
        result = "Что-то пошло не так .. "
    context = {
        'now_year': now_year,
        'fromdate': fromdate,
        'todate': todate,
        'operationss': operationss,
        'quotations': quotations,
        'menu': menu,
        "title": "Котировки",
        'result': result,
        'day': day,
        'end_date2': end_date2,
        'typed': typed,
        'typedd': typedd,
        'end_date': end_date,

    }
    return render(request, 'crm_app/quotations_for_period.html', context=context)
#
# =
# =========================sdelki by period==========================
def sdelki_for_period(request, sdelki=None):
   # sdelki = Sdelka.objects.all()
    if request.method == "POST":
        fromdate = request.POST.get('fromdate')
        todate = request.POST.get('todate')
        day = timedelta(minutes=60 * 24)
        end_date = datetime.today() + timedelta(days=1)
        typed = type(day)
        end_date2 = end_date.strftime("%d.%m.%Y")
        typedd = type(todate)
        sdelki = Sdelka.objects.raw(
            'select * from crm_app_sdelka where time_create between "' + fromdate + '" and "' + todate + '"')

    else:
        result = "Что-то пошло не так .. "
    context = {
        'now_year': now_year,
        'fromdate': fromdate,
        'todate': todate,
        'operationss': operationss,
        'sdelki': sdelki,
        'menu': menu,
        "title": "Сделки",

        'day': day,
        'end_date2': end_date2,
        'typed': typed,
        'typedd': typedd,
        'end_date': end_date,
    }
    return render(request, 'crm_app/sdelki_for_period.html', context=context)



# =========search supplyer by date =========
'''
def supplyers_search(request):
    supplyers = Supplyer.objects.all()
    earlier_supplyer = Supplyer.objects.earliest('time_create')
    latest_supplyer = Supplyer.objects.latest('time_create')
    # now = datetime.now() - timedelta(minutes=60 * 24 * 7)  # 60*24---это сутки
    # result = Supplyer.objects.filter(time_create__lte='2023-12-10', time_create__gte='2023-12-01')
    context = {
        'now_year': now_year,
        'earlier_supplyer': earlier_supplyer,
        'latest_supplyer': latest_supplyer,
        'operationss': operationss,
        'supplyers': supplyers,
        'menu': menu,
        "title": "Перевозчики",
    }
    return render(request, 'crm_app/supplyers_search.html', context=context)


def clients_search(request):
    clients = Client.objects.all()
    earlier_client = Client.objects.earliest('time_create')
    latest_client = Client.objects.latest('time_create')
    context = {
        'now_year': now_year,
        'earlier_client': earlier_client,
        'latest_client': latest_client,
        'contragentss': contragentss,
        'clients': clients,
        'menu': menu,
        "title": "Заказчики",
    }
    return render(request, 'crm_app/clients_search.html', context=context)


# =========  search квотейшн by date =========
def quotations_search(request):
    quotations = Quotation.objects.all()
    earlier_quotation = Quotation.objects.earliest('time_create')
    latest_quotation = Quotation.objects.latest('time_create')
    context = {
        'now_year': now_year,
        'earlier_quotation': earlier_quotation,
        'latest_quotation': latest_quotation,
        'operationss': operationss,
        'quotations': quotations,
        'menu': menu,
        "title": "Котировки",
    }
    return render(request, 'crm_app/quotations_search.html', context=context)



def sdelki_search(request):
    sdelki = Quotation.objects.all()
    earlier_sdelka = Sdelka.objects.earliest('time_create')
    latest_sdelka = Sdelka.objects.latest('time_create')
    context = {
        'now_year': now_year,
        'earlier_sdelka': earlier_sdelka,
        'latest_sdelka': latest_sdelka,
        'contragentss': contragentss,
        'operationss': operationss,
        'sdelki': sdelki,
        'menu': menu,
        "title": "Сделки",
    }
    return render(request, 'crm_app/sdelki_search.html', context=context)
'''

# =============end serching======================


def show_sdelka(request, c_id):
    sdelka = get_object_or_404(Sdelka, pk=c_id)

    url = resolve(request.path_info).url_name
    sdelki = Sdelka.objects.all()

    # ~Q(currency1=2) | ~Q(cusdelkarrency1=2) | ~Q(currency1=2) | ~Q(currency1=2) | ~Q(currency1=2) | ~Q(currency1=2) |)

    context = {
        'now_year': now_year,
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
        'now_year': now_year,

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
    agr_f = Sdelka.objects.aggregate(Max('client_currency'))
    agr_f2 = Sdelka.objects.aggregate(Max('client_currency'), Min('client_currency'))
    valu = Sdelka.objects.values('supplyer_1', 'supplyer_2', 'supplyer_3', 'supplyer_4', 'supplyer_5',
                                 'supplyer_6', ).filter(pk__gt=2)
    efe = Sdelka.objects.filter(client_currency__gt=F('currency1'))  # сумма клиента больше ілі = суммы перевозчика

    context = {
        'now_year': now_year,
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


# ========================


def quotations(request):
    quotations = Quotation.objects.all()

    context = {
        'now_year': now_year,
        'operationss': operationss,
        'quotations': quotations,
        'menu': menu,
        "title": "Котировки",
    }
    return render(request, 'crm_app/quotations.html', context=context)


def sdelki(request):
    sdelki = Sdelka.objects.all()
    euro = Currency.objects.get(id=2)

    context = {
        'now_year': now_year,
        'operationss': operationss,
        'sdelki': sdelki,
        'menu': menu,
        "title": "Сделки",
    }
    return render(request, 'crm_app/sdelki.html', context=context)


def login(request):
    return render(request, 'crm_app/login.html', {'menu': menu, "title": "Войти"})


#=======add document======
def document_itself(request):
    document = get_object_or_404(Documents)
    form = DocumentSdelkaSupplyerForm(request.POST or None,
                                      instance=document)
    url = resolve(request.path_info).url_name
    context = {
        'now_year': now_year,
        'operationss': operationss,
        'documentss': documentss,
        'menu': menu,
        "title": "Редактирование документа",
        'form': form,
        'document': document,
        'url': url,
    }
    if form.is_valid():
        form.save()
        messages.success(request, 'file добавлен')
        return redirect('documents')
    return render(request, 'crm_app/document_itself.html', context=context)

#============
def add_client(request):
    if request.method == 'POST':
        form = AddClientForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Заказчик добавлен')
            return redirect('clients')
    else:
        form = AddClientForm()

    return render(request, 'crm_app/add_client.html', {'form': form, 'menu': menu, 'title': 'Создать Заказчика'})


# ======

def add_supplyer(request):
    if request.method == 'POST':
        form = AddSupplyerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('supplyers')
    else:
        form = AddSupplyerForm()
        messages.success(request, 'Перевозчик добавлен')
    return render(request, 'crm_app/add_supplyer.html', {'form': form, 'menu': menu, 'title': 'Создать Перевозчика'})


def add_othercompany(request):
    if request.method == 'POST':
        form = AddOtherCompanyForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Организация добавлена')
            return redirect('other_companies')
    else:
        form = AddOtherCompanyForm()
    return render(request, 'crm_app/add_othercompany.html',
                  {'form': form, 'menu': menu, 'title': 'Создать Стороннюю Организацию'})


# ================================
# =========================================
def quot_sdelka(request, c_id):
    sdelka = get_object_or_404(Quotation, pk=c_id)
    quotation = get_object_or_404(Quotation, pk=c_id)
    form = AddSdelkaForm(request.POST or None, instance=quotation)
    url = resolve(request.path_info).url_name
    quotations = Quotation.objects.all()
    context = {
        'now_year': now_year,
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

# ===add documents !!!!!!!!!!!!!!!!!!!!!!!!!!!!
def document_itself(request):
    document = Documents.objects.all()
    if request.method == "POST":
        form = UploadDocumentsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'file добавлен')
            return redirect('documents')
    else:
        form=UploadDocumentsForm()

    context = {
        'now_year': now_year,
        'operationss': operationss,
        'documentss': documentss,
        'menu': menu,
        "title": "Добавление документа",
        'form': form,
        'document': document,
    }

    return render(request, 'crm_app/document_itself.html', context=context)


# =============Forms add+++++++++++++++++
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
    context = {
        'now_year': now_year,
        'operationss': operationss,
        'sdelki': sdelki,
        'menu': menu,
        "title": "Добавить Сделку",
        'form': form,
    }
    return render(request, 'crm_app/add_sdelka.html', context=context)


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
    context = {
        'now_year': now_year,
        'operationss': operationss,
        'sdelki': sdelki,
        'menu': menu,
        "title": "Добавить котировку",
        'form': form,
    }

    return render(request, 'crm_app/add_quotation.html', context=context)





def document_sdelka_supplyer(request, c_id):
    documents = Documents.objects.all()
    sdelka = get_object_or_404(Sdelka, pk=c_id)
    form = DocumentSdelkaSupplyerForm(request.POST or None, initial={'sdelka': sdelka, 'supplyer': sdelka.supplyer_1}, instance=sdelka)
    url = resolve(request.path_info).url_name
    context = {
        'now_year': now_year,
        'operationss': operationss,
        'documents': documents,
        'menu': menu,
        "title": "Добавить документ от Перевозчика",
        'form': form,
        'sdelka': sdelka,
        'url': url,
    }
    if form.is_valid():
        form.save()
        messages.success(request, 'file добавлен')
        return redirect('sdelki')

    return render(request, 'crm_app/document_sdelka_supplyer.html', context=context)
#====

####===========

def document_sdelka_client(request, c_id):
    documents = Documents.objects.all()
    sdelka = get_object_or_404(Sdelka, pk=c_id)
    form = DocumentSdelkaClientForm(request.POST or None, initial={'sdelka': sdelka}, instance=sdelka)
    url = resolve(request.path_info).url_name
    context = {
        'now_year': now_year,
        'operationss': operationss,
        'documents': documents,
        'menu': menu,
        "title": "Добавить документ от Заказчика",
        'form': form,
        'sdelka': sdelka,
        'url': url,
    }
    if form.is_valid():
        form.save()
        messages.success(request, 'file добавлен')
        return redirect('sdelki')

    return render(request, 'crm_app/document_sdelka_client.html', context=context)
#====

#==========delete document++++++++

def download_document(request):
    documents = Documents.objects.all()
    form = None
    if request.method == "POST":
        form = UploadDocumentsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            print(form.cleaned_data)
            messages.success(request, 'file добавлен')
            return redirect('sdelki')
    else:
        form = UploadDocumentsForm()
    context = {
        'now_year': now_year,
        'operationss': operationss,
        'documents': documents,
        'menu': menu,
        "title": "Добавить документ",
        'form': form,
    }
    return render(request, 'crm_app/download_document.html', context=context)





def supplyers_docs(request):
    sdelki = Sdelka.objects.all()
    documents = Documents.objects.all()
    dogovory = Documents.objects.filter(type='Договор')
    '''for choosing clients files'''
    documents = Documents.objects.annotate(len=Length('supplyer'))
    context = {
        'now_year': now_year,
        'sdelki': sdelki,
        'menu': menu,
        'documents': documents,
        'documentss': documentss,
        "title": "Документы Перевозчиков",
        'dogovory': dogovory,
        'clients_docs': clients_docs,
    }
    return render(request, 'crm_app/clients_docs.html', context=context)

def other_companies_docs(request):
    sdelki = Sdelka.objects.all()
    documents = Documents.objects.all()
    dogovory = Documents.objects.filter(type='Договор')
    '''for choosing clients files'''
    documents = Documents.objects.annotate(len=Length('other_company'))
    context = {
        'now_year': now_year,
        'sdelki': sdelki,
        'menu': menu,
        'documents': documents,
        'documentss': documentss,
        "title": "Документы Сторонних Организаций",
        'dogovory': dogovory,
        'clients_docs': clients_docs,
    }
    return render(request, 'crm_app/clients_docs.html', context=context)

#===========================================================
def upload_documents(request):
    sdelki = Sdelka.objects.all()
    documents = Documents.objects.all()
    dogovory = Documents.objects.filter(type='Договор')
    '''for choosing clients files'''
    clients_docs=Documents.objects.annotate(len=Length('client'))
    '''for choosing supplyers files'''
    supplyers_docs = Documents.objects.annotate(len=Length('supplyer'))
    '''for choosing other_organizations files'''
    other_companies_docs = Documents.objects.annotate(len=Length('other_company'))

    if request.method == 'POST':
        form = UploadDocumentsForm(request.POST, request.FILES)
        # file = request.FILES.getlist('file')[1]
        file = request.FILES['file']
        client = Client.objects.get(pk=1)
        supplyer1 = Supplyer.objects.get(pk=1)
        print(client)
        print(supplyer1)
        client_document = Sdelka.objects.create(client=client, supplyer1=supplyer1, cl_documents=file)
        client_document.save()
        return HttpResponse('file added to sdelka: ' + str(client_document.pk))
    else:
        form = UploadDocumentsForm()

        context = {
            'now_year': now_year,
            'form': form,
            'operationss': operationss,
            'sdelki': sdelki,
            'menu': menu,
            'documents': documents,
            'documentss': documentss,
            "title": "Документы",
            'dogovory': dogovory,
            'clients_docs': clients_docs,
            'other_companies_docs': other_companies_docs,
            'supplyers_docs': supplyers_docs,

        }
    return render(request, 'crm_app/documents.html', context=context)


#----------GENERATE excel  FILE----------------
def to_excel(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] ='attachment; filename=.vypiska.csv'
    # designet a model
    writer = csv.writer(response)
    sdelki = Sdelka.objects.all()

    writer.writerow(['заказчик','перевозчик'])

    for s in sdelki:
        writer.writerow([s.client,  s.supplyer_1])

    return response



def extract(request, pk):
    sdelki = Sdelka.objects.all()
    response = HttpResponse(content_type='text/plain')
    response['Content-Disposition'] ='attachment; filename=vypiska_sdelki.txt'
    # designet a model
    url = resolve(request.path_info).url_name

    sdelka = get_object_or_404(Sdelka, pk=pk)
    lin = '-' * 110
    space = " " * 4

    # create lines:
    lines = [f"{lin}\n",
           f"Заказчик {space}{space} Сумма заказчика {space} Валюта\n",
           f"{lin}\n",
           ]
     # for s in sdelki:
    if pk == 1:

        sdelki = sdelki.filter(number=12)
        for a in sdelki:
            a.cl=str(a.client)
            lines.append(f"{a.cl:>15}   {a.client_price:15}    {a.client_currency}\n")
    elif pk == 3:
        sdelki = sdelki.filter(number=5)
        for a in sdelki:
            a.cl=str(a.client)
            lines.append(f"{a.cl:>15}   {a.client_price:15}    {a.client_currency}\n")
    elif pk == 2:
        sdelki = sdelki.filter(number=5)
        for a in sdelki:
            a.cl=str(a.client)
            lines.append(f"{a.cl:>15}   {a.client_price:15}    {a.client_currency}\n")
    response.writelines(lines)

    return response

now = datetime.now() - timedelta(minutes=60 * 24 * 7)  # 60*24---это сутки*7  =неделя
six = six_months_period()
three = period_quartal()
sd = Sdelka.objects.all()
sd_quartal = Sdelka.objects.filter(time_create__gte=three)
sd_six = Sdelka.objects.filter(time_create__gte=six)
sd_week = Sdelka.objects.filter(time_create__gte=now)

#============ВЫПИСКА ВСЕ СДЕЛКИ===============

def dinamic_file_all_sdelki(request):
    sdelki = sd
    response = HttpResponse(content_type='text/plain')
    response['Content-Disposition'] = 'attachment; filename=vypiska_all.txt'
    lin = '-' * 110
    space = " " * 4
    lines = [f"{lin}\n",
             f"Выписка за весь период \n"
             f"{lin}\n",
             f"{space} Заказчик{space} Сумма заказчика {space} Валюта\n",
             f"{lin}\n",
             ]
    for s in sdelki:
        s.cl = str(s.client)
        lines.append(f"{s.cl:>15}   {s.client_price:15}    {s.client_currency}\n")

    response.writelines(lines)

    return response

#============  ВЫПИСКА 3 МЕСЯЦА ===============
def dinamic_file_quartal_sdelki(request):
    sdelki = sd_quartal
    response = HttpResponse(content_type='text/plain')
    response['Content-Disposition'] = 'attachment; filename=vypiska_quartal.txt'
    lin = '-' * 110
    space = " " * 4
    lines = [f"{lin}\n",
             f"Выписка за: 3 месяца\n"
             f"{lin}\n",
             f"{space} Заказчик{space} Сумма заказчика {space} Валюта\n",
             f"{lin}\n",
             ]
    for s in sdelki:
        s.cl = str(s.client)
        lines.append(f"{s.cl:>15}   {s.client_price:15}    {s.client_currency}\n")

    response.writelines(lines)

    return response

#===============  six month  ============
def dinamic_file_six_sdelki(request):
    sdelki = sd_six
    response = HttpResponse(content_type='text/plain')
    response['Content-Disposition'] = 'attachment; filename=vypiska_half_year.txt'
    lin = '-' * 110
    space = " " * 4
    lines = [f"{lin}\n",
             f"Выписка за: 6 месяцев\n"
             f"{lin}\n",
             f"{space} Заказчик{space} Сумма заказчика {space} Валюта\n",
             f"{lin}\n",
             ]
    for s in sdelki:
        s.cl = str(s.client)
        lines.append(f"{s.cl:>15}   {s.client_price:15}    {s.client_currency}\n")

    response.writelines(lines)

    return response

#================= vypiska week  ===================
def dinamic_file_week_sdelki(request):
    sdelki = sd_week
    response = HttpResponse(content_type='text/plain')
    response['Content-Disposition'] = 'attachment; filename=vypiska_week.txt'
    lin = '-' * 110
    space = " " * 4
    lines = [f"{lin}\n",
             f"Выписка за: 7 дней \n"
             f"{lin}\n",
             f"{space} Заказчик{space} Сумма заказчика {space} Валюта\n",
             f"{lin}\n",
             ]
    for s in sdelki:
        s.cl = str(s.client)
        lines.append(f"{s.cl:>15}   {s.client_price:15}    {s.client_currency}\n")

    response.writelines(lines)

    return response



