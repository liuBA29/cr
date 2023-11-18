from django.contrib import admin
from .models import *


class SupplyerAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'phone')

class QuotationAdmin(admin.ModelAdmin):
    list_display = ('time_create', 'client', 'loading_country', 'status')


class SdelkaAdmin(admin.ModelAdmin):
    list_display = ('descripsion', 'client', 'cl_documents', 'sup_documents')


admin.site.register(Client)

admin.site.register(Supplyer, SupplyerAdmin)


admin.site.register(OtherCompany)
admin.site.register(Money)
admin.site.register(Currency)
admin.site.register(Direction)
admin.site.register(Transport)
admin.site.register(Quotation, QuotationAdmin)
admin.site.register(Sdelka, SdelkaAdmin)