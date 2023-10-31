from django.urls import path
from crm_app.views import  *

urlpatterns = [
    path('', index, name='home'),
    path('contragents/', contragents, name='contragents'),
    path('clients/', clients, name='clients'),
    path('supplyers/', supplyers, name='supplyers'),
    path('other_companies/', other_companies, name='other_companies'),

    path('contragent/<int:c_id>/', show_contragent, name='show_contragent'),


    path('operations/', operations, name='operations'),
    path('login/', login, name='login'),
    path('add_sdelka/', add_sdelka, name='add_sdelka'),
    path('add_stavka/', add_stavka, name='add_stavka'),
]

