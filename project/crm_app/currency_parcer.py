import requests
#from bs4 import BeautifulSoup
from pprint import pprint
from .models import  *

#pprint(response)

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

                result_euro = f'({result_byn/euro_rate} )'
                return result_euro


# our_cur = find_currency('RUB')
# print(our_cur)