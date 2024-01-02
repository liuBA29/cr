import requests
#from bs4 import BeautifulSoup
from pprint import pprint

from django.http import HttpResponse

from .models import  *

    # counting profit function:
def show_profit(supl_pr, client_pr):
    profit = 0
    if type(supl_pr) == int or type(supl_pr) == float:
        if type(client_pr)  == int or type(client_pr) == float:
            profit = supl_pr - client_pr
            return f"{profit:.2f}"
    else:
        return

    # counting price in euro function:
def find_currency(Cur_Abbreviation, price):
    url = 'https://api.nbrb.by/exrates/rates?periodicity=0'
    #price = 25
    response = requests.get(url).json()
    euro_rate = response[9]['Cur_OfficialRate']
    for item in response:
        if Cur_Abbreviation == 'BYR':
            result_euro=price/euro_rate
            return  result_euro
        else:
            result_byn = price / item["Cur_Scale"] * item["Cur_OfficialRate"]
            if Cur_Abbreviation in item["Cur_Abbreviation"]:

                result_euro = result_byn/euro_rate
                return result_euro


# our_cur = find_currency('RUB')
# print(our_cur)

def qf_vypiska():
    qf = Qfilter.objects.latest('created')
    sdelki = []
    response = HttpResponse(content_type='text/plain')
    response['Content-Disposition'] = 'attachment; filename=vypiska_week.txt'
    lin = '-' * 220
    space = " " * 4
    lines = [f"{lin}\n",
             f'Выписка СДЕЛОК поиска о описанию: " {qf.qfilter} "\n',
             f"{lin}\n",
             f"{space}Заказчик{space} Сумма заказчика  Валюта{space}",
             f"{space}Перевозчик1 {space}{space}{space} Сумма Валюта{space} Дата разгрузки{space} {space}Дебиторка"
             f"{space}Профит,EUR{space}Направление {space} Транспорт\n",
            f"\n",
             ]
    #counting tthe quontitty of supplyers in Sdelka:
    actual_sup_list = []
    #список перевозчиков
    sup_count_list=[]
    sup2 = sdelki.values('supplyer_2').exclude(supplyer_2=None)
    sup2_count = sup2.count()
    if sup2_count > 0:
        sup_count_list.append('Перевозчик2')
        actual_sup_list.append('supplyer_2')
    sup3 = sdelki.values('supplyer_3').exclude(supplyer_3=None)
    sup3_count = sup3.count()
    if sup3_count > 0:
        sup_count_list.append('Перевозчик3')
        actual_sup_list.append('supplyer_3')
    sup4 = sdelki.values('supplyer_4').exclude(supplyer_4=None)
    sup4_count = sup4.count()
    if sup4_count > 0:
        sup_count_list.append('Перевозчик4')
        actual_sup_list.append('supplyer_4')
    sup5 = sdelki.values('supplyer_5').exclude(supplyer_5=None)
    sup5_count = sup5.count()
    if sup5_count > 0:
        sup_count_list.append('Перевозчик5')
        actual_sup_list.append('supplyer_5')
    sup6 = sdelki.values('supplyer_6').exclude(supplyer_6=None)
    sup6_count = sup6.count()
    if sup6_count > 0:
        sup_count_list.append('Перевозчик6')

    sup7 = sdelki.values('supplyer_7').exclude(supplyer_7=None)
    sup7_count = sup7.count()
    if sup7_count > 0:
        sup_count_list.append('Перевозчик7')
    sup8 = sdelki.values('supplyer_8').exclude(supplyer_8=None)
    sup8_count = sup8.count()
    if sup8_count > 0:
        sup_count_list.append('Перевозчик8')
    sup9 = sdelki.values('supplyer_9').exclude(supplyer_9=None)
    sup9_count = sup9.count()
    if sup9_count > 0:
        sup_count_list.append('Перевозчик9')
    sup10 = sdelki.values('supplyer_10').exclude(supplyer_10=None)
    sup10_count = sup10.count()
    if sup10_count > 0:
        sup_count_list.append('Перевозчик10')
# добавление существующих категорий перевозчикв в шапку
#     for p in sup_count_list:
#         lines.append(f"{space}{space}{p}{space}{space} Сумма{space}Валюта ")


    # lines.append(f"Дата разгрузки{space} Профит, EUR{space}Транспорт{space}Направление{space}Дебиторка\n")
    # lines.append(f'{lin}\n ')

    for s in sdelki:
        s.cl = str(s.client)
        s.cl_cur=str(s.client_currency)
        # переводим цену заказчика в евро:
        s.price_into_eur = str(find_currency(str(s.client_currency), s.client_price))


        # переводим цену ПЕРЕВОЗЧИКОВ в евро:

        s.sup1 = str(s.supplyer_1)
        s.sub_cur1 = str(s.currency1)
        s.sup1_price_into_eur = str(find_currency(str(s.currency1), s.sup_price_1))

        s.price_into_eur_fl = find_currency(str(s.client_currency), s.client_price)
        s.sup1_price_into_eur_fl = find_currency(str(s.currency1), s.sup_price_1)
        profit = str(show_profit(s.sup1_price_into_eur_fl, s.price_into_eur_fl))

        s.sup2_price_into_eur = str(find_currency(str(s.currency2), s.sup_price_2))
        s.sup2 = str(s.supplyer_2)
        s.razgruzka = str(s.data_zagruzki_1)

        transport=str(s.common_transport)
        direction = str(s.common_direction)

        lines.append(f"{s.cl:>18}  {s.client_price:>10}    {s.cl_cur:5} "
                     f"{s.sup1:>22}   {s.sup_price_1:>12}    {s.sub_cur1:5}     {s.razgruzka:15}  "
                     f"      {s.debitorka1:>5}  {profit:>12} {direction:>12} {transport:>20}\n")

# добавляем других перевозчиков:
        #if sup2_count > 0:
           #s.sup2_price_into_eur = str(find_currency(str(s.currency2), s.sup_price_2))
            #s.sup2 = str(s.supplyer_2)
            #s.cl_cur2 = str(s.currency2)
            #lines.append(f" {s.sup2:>20} {s.sup_price_2:>12}    {s.cl_cur2:5}   {s.data_vygruzki_2}")
        #else:
           # lines.append("\n")
        #lines.append(find_currency('CNY', s.client_price))
    lines.append(f"{lin}\n")
    lines.append(f"Профит высчитывается: СУММА ПЕРЕВОЗЧИКА,eur  -  СУММА ЗАКАЗЧИКА,eur\n")
    lines.append(f"\n")
    lines.append(f'{lin}\n   \n this is the end...')

    response.writelines(lines)
    return response


def spisok_perevozchikov():
    return True


