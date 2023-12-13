from django.test import TestCase
import datetime
import calendar
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta


date = datetime(year=2023, month=11, day=2)
last_day = date + relativedelta(day=31)

now = datetime.today()




print('last day')
print(date)
print('date_six')




#six_month=sdelki.filter(time_create__gte=now)
now = datetime.now() - timedelta(minutes=60 * 24 * 7)  # 60*24---это сутки
#sdelki = sdelki.filter(time_create__gte=now)


date_six = datetime(now.year, month=12, day=12)

last_day_six = date_six + relativedelta(day=31)

print(last_day_six.day)

def period_quartal():
    '''считаем период за квартал'''
    m1, m2, m3 = 0, 0, 0

    period = datetime.now() - timedelta(days=30)
    #period.month  period.year
    m = datetime(period.year, period.month, day=12)
    '''дней первого месяца ...'''
    m1 = m + relativedelta(day=31)
    m1 = m1.day
    period = period - timedelta(days=m1)
    m = datetime(period.year, period.month, day=12)
    m2 = m + relativedelta(day=31)
    m2 = m2.day
    period = period - timedelta(days=m2)
    m = datetime(period.year, period.month, day=12)
    m3 = m + relativedelta(day=31)
    m3 = m3.day
    result = datetime.now() - timedelta(days=m1 + m2 + m3)
    print(result)
    print(m.month, "---m" )
    return result


def six_months_period():
    '''считаем период за 6 месяцев'''
    m1, m2, m3, m4, m5, m6 = 0, 0, 0, 0, 0, 0

    period = datetime.now() - timedelta(days=30)
    #period.month  period.year
    m = datetime(period.year, period.month, day=12)
    '''дней первого месяца ...'''
    m1 = m + relativedelta(day=31)
    m1 = m1.day
    period = period - timedelta(days=m1)
    m = datetime(period.year, period.month, day=12)
    m2 = m + relativedelta(day=31)
    m2 = m2.day
    period = period - timedelta(days=m2)
    m = datetime(period.year, period.month, day=12)
    m3 = m + relativedelta(day=31)
    m3 = m3.day
    period = period - timedelta(days=m3)
    m = datetime(period.year, period.month, day=12)
    m4 = m + relativedelta(day=31)
    m4 = m4.day
    period = period - timedelta(days=m4)
    m = datetime(period.year, period.month, day=12)
    m5 = m + relativedelta(day=31)
    m5 = m5.day
    period = period - timedelta(days=m5)
    m = datetime(period.year, period.month, day=12)
    m6 = m + relativedelta(day=31)
    m6 = m6.day
    result = datetime.now() - timedelta(days=m1 + m2 + m3 + m4 + m5 + m6)
    print(result)
    print("m1--", m1, "m2--", m2, "m3--", m3)
    return result
    # print("m1--", m1, "m2--", m2, "m3--", m3, "m4--", m4, "m5--", m5, "m6--", m6)

    # print(datetime.now())


six_month = datetime.now() - timedelta(days=30+30+31)
#print(six_month)
now = datetime.today()
#print(now)
six_months_period()
period_quartal()