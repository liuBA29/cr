from django.contrib import admin
from .models import *


class SupplyerAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'phone')

class QuotationAdmin(admin.ModelAdmin):
    list_display = ( 'client', 'loading_country', 'status')


class SdelkaAdmin(admin.ModelAdmin):
    list_display = ('description', 'client')


admin.site.register(Client)

admin.site.register(Supplyer, SupplyerAdmin)


admin.site.register(OtherCompany)
admin.site.register(Documents)
admin.site.register(Currency)
admin.site.register(Direction)
admin.site.register(Transport)
admin.site.register(Quotation, QuotationAdmin)
admin.site.register(Sdelka, SdelkaAdmin)