from django.contrib import admin
from .models import *


class SupplyerAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'phone')

class StavkaAdmin(admin.ModelAdmin):
    list_display = ( 'transport', 'direction', 'price')


class SdelkaAdmin(admin.ModelAdmin):
    list_display = ( 'descripsion', 'client')


admin.site.register(Client)

admin.site.register(Supplyer, SupplyerAdmin)

admin.site.register(Stavka, StavkaAdmin)
admin.site.register(OtherCompany)
admin.site.register(Money)
admin.site.register(Sdelka, SdelkaAdmin)