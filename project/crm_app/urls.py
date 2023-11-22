from django.urls import path
from crm_app.views import  *
from django.conf import settings



urlpatterns = [
    path('', index, name='home'),
    path('contragents/', contragents, name='contragents'),
    path('clients/', clients, name='clients'),
    path('supplyers/', supplyers, name='supplyers'),
    path('other_companies/', other_companies, name='other_companies'),


    path('client/<int:c_id>/', show_client, name='show_client'),
    path('supplyer/<int:c_id>/', show_supplyer, name='show_supplyer'),
    path('other_company/<int:c_id>/', show_other_company, name='show_other_company'),


    path('quotation/<int:c_id>/', show_quotation, name='show_quotation'),
    path('sdelka/<int:c_id>/', show_sdelka, name='show_sdelka'),

    path('update_quotation/<int:c_id>/', update_quotation, name='update_quotation'),
    path('update_sdelka/<int:c_id>/', update_sdelka, name='update_sdelka'),
    path('quot_sdelka/<int:c_id>/', quot_sdelka, name='quot_sdelka'),

    path('delete_quotation/<int:c_id>/', delete_quotation, name='delete_quotation'),
    path('delete_sdelka/<int:c_id>/', delete_sdelka, name='delete_sdelka'),
    path('delete_client/<int:c_id>/', delete_client, name='delete_client'),
    path('delete_supplyer/<int:c_id>/', delete_supplyer, name='delete_supplyer'),
    path('delete_other_company/<int:c_id>/', delete_other_company, name='delete_other_company'),


    path('operations/', operations, name='operations'),
    path('quotations/', quotations, name='quotations'),
    path('sdelki/', sdelki, name='sdelki'),


    path('login/', login, name='login'),
    path('add_client/', add_client, name='add_client'),
    path('add_supplyer/', add_supplyer, name='add_supplyer'),
    path('add_othercompany/', add_othercompany, name='add_othercompany'),

    path('add_sdelka/', add_sdelka, name='add_sdelka'),
    path('add_quotation/', add_quotation, name='add_quotation'),


    path('documents/', upload_documents, name='documents'),

    path('extract/', sdelka_vypiska, name='extract'),





]

