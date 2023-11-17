from django.urls import path
from crm_app.views import  *

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
    path('delete_quotation/<int:c_id>/', delete_quotation, name='delete_quotation'),


    path('operations/', operations, name='operations'),
    path('quotations/', quotations, name='quotations'),
    path('sdelki/', sdelki, name='sdelki'),


    path('login/', login, name='login'),
    path('add_sdelka/', add_sdelka, name='add_sdelka'),
    path('add_quotation/', add_quotation, name='add_quotation'),
]

