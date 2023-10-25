from django.urls import path
from crm_app.views import  *

urlpatterns = [
    path('', index, name='home'),
    path('contragents/', contragents, name='contragents'),
    path('operations/', operations, name='operations'),
    path('login/', login, name='login'),

]

