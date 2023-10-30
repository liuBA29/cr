from django.shortcuts import render, HttpResponse


menu =[
    {'title': 'Главная', 'url_name': 'home'},
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



#=============Forms add