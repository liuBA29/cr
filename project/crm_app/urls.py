from django.urls import path


from .views import *

urlpatterns = [
    path('', index),
]


from crm_app.views import  *
from django.conf import settings
import calendar
from calendar import HTMLCalendar



urlpatterns = [

    path('', index, name='home'),
    path('not_allowed', redirect_crm, name="not_allowed"),

    path('<int:year>/<str:month>/', index, name='home'),

    path('contragents/', contragents, name='contragents'),
    path('clients/', clients, name='clients'),
    path('supplyers/', supplyers, name='supplyers'),

    path('clients_for_period/', clients_for_period, name='clients_for_period'),
    path('supplyers_for_period/', supplyers_for_period, name='supplyers_for_period'),

  #  path('clients_search/', clients_search, name='clients_search'),
   # path('supplyers_search/', supplyers_search, name='supplyers_search'),

    path('other_companies/', other_companies, name='other_companies'),


    path('client/<int:c_id>/', show_client, name='show_client'),
    path('supplyer/<int:c_id>/', show_supplyer, name='show_supplyer'),
    path('other_company/<int:c_id>/', show_other_company, name='show_other_company'),
    path('document/<int:c_id>/', show_document, name='show_document'),


    path('quotation/<int:c_id>/', show_quotation, name='show_quotation'),
    path('sdelka/<int:c_id>/', show_sdelka, name='show_sdelka'),

    path('quotations_for_period/', quotations_for_period, name='quotations_for_period'),
    path('sdelki_for_period/', sdelki_for_period, name='sdelki_for_period'),
  #  path('quotations_search/', quotations_search, name='quotations_search'),
   # path('sdelki_search/', sdelki_search, name='sdelki_search'),

    path('update_quotation/<int:c_id>/', update_quotation, name='update_quotation'),
    path('update_sdelka/<int:c_id>/', update_sdelka, name='update_sdelka'),
    path('quot_sdelka/<int:c_id>/', quot_sdelka, name='quot_sdelka'),
    path('update_client/<int:c_id>/', update_client, name='update_client'),
    path('update_supplyer/<int:c_id>/', update_supplyer, name='update_supplyer'),
    path('update_other_company/<int:c_id>/', update_other_company, name='update_other_company'),
    path('document_itself/', document_itself, name='document_itself'),




    path('delete_document/<int:c_id>/', delete_document, name='delete_document'),
    path('delete_quotation/<int:c_id>/', delete_quotation, name='delete_quotation'),
    path('delete_sdelka/<int:c_id>/', delete_sdelka, name='delete_sdelka'),
    path('delete_client/<int:c_id>/', delete_client, name='delete_client'),
    path('delete_supplyer/<int:c_id>/', delete_supplyer, name='delete_supplyer'),
    path('delete_other_company/<int:c_id>/', delete_other_company, name='delete_other_company'),


    path('operations/', operations, name='operations'),
    path('quotations/', quotations, name='quotations'),
    path('sdelki/', sdelki, name='sdelki'),


    path('supplyers/<int:pk>/', supplyers_filter, name='supplyers_filter'),
    path('clients/<int:pk>/', clients_filter, name='clients_filter'),
    path('quotations/<int:pk>/', quotations_filter, name='quotations_filter'),
    path('sdelki/<int:pk>/', sdelki_filter, name='sdelki_filter'),

    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('add_client/', add_client, name='add_client'),
    path('add_supplyer/', add_supplyer, name='add_supplyer'),


    path('supplyer_list/', ClassicSearchSupplyer.as_view(), name='classic_search_supplyer'),
    path('client_list/', ClassicSearchClient.as_view(), name='classic_search_client'),
    path('quotation_list/', ClassicSearchQuotation.as_view(), name='classic_search_quotation'),
    path('sdelka_list/', ClassicSearchSdelka.as_view(), name='classic_search_sdelka'),


    path('add_othercompany/', add_othercompany, name='add_othercompany'),

    path('add_sdelka/', add_sdelka, name='add_sdelka'),
    path('add_quotation/', add_quotation, name='add_quotation'),


    path('documents/', upload_documents, name='documents'),
    path('docs_types/<int:pk>', docs_types, name='docs_types'),
    path('docs_types_supplyers/<int:pk>', docs_types_supplyers, name='docs_types_supplyers'),
    path('docs_types_other_companies/<int:pk>', docs_types_other_companies, name='docs_types_other_companies'),
    path('clients_docs/', clients_docs, name='clients_docs'),
    path('supplyers_docs/', supplyers_docs, name='supplyers_docs'),

    path('other_companies_docs/', other_companies_docs, name='other_companies_docs'),
    path('download_document/', download_document, name='download_document'),




    path('document_sdelka_client/<int:c_id>/', document_sdelka_client, name='document_sdelka_client'),
    path('document_sdelka_supplyer/<int:c_id>/', document_sdelka_supplyer, name='document_sdelka_supplyer'),

    # выписки по сделкам
    path('extract/<int:pk>/', extract, name='extract'),
    path('to_excel/', to_excel, name='to excel'),
    path('dinamic_file/3', dinamic_file_quartal_sdelki, name='dinamic_file_quartal_sdelki'),
    path('dinamic_file/6', dinamic_file_six_sdelki, name='dinamic_file_six_sdelki'),
    path('dinamic_file/', dinamic_file_all_sdelki, name='dinamic_file_all_sdelki'),
    path('dinamic_file/1', dinamic_file_week_sdelki, name='dinamic_file_week_sdelki'),

    path('calendar_filter/pk', calendar_filter, name='calendar_filter'),
   # path('some_view/', some_view, name='some_view'),qf
    path('qf_vypiska/', qf_vypiska, name='qf_vypiska'),

   path('api/v1/clients/', ClientAPIView.as_view(), name='clientapi'),
   path('api/v1/clients/<int:pk>/', ClientAPIUpdate.as_view(), name='clientapiupdate'),
   path('api/v1/supplyers/', SupplyerAPIList.as_view()),
   path('api/v1/supplyers/<int:pk>/', SupplyerAPIUpdate.as_view()),

    path('api/v1/sdelki/', SdelkaAPIList.as_view()),
    path('api/v1/sdelki/<int:pk>/', SdelkaAPIUpdate.as_view()),

    path('cb1/', CallbackView.as_view(), name='cb1'),

 ]


