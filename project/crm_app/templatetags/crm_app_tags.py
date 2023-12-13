from crm_app.models import  *
from django import  template
import datetime

from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta


register= template.Library()

@register.simple_tag()
def get_sdelki(filter=None):
    if not filter:
        return Sdelka.objects.all()
    else:
        return Sdelka.objects.filter(filter)


@register.simple_tag()
def six_month():
    '''считаем период за 6 месяцев'''
    m1, m2, m3, m4, m5, m6 = 0, 0, 0, 0, 0, 0
    period = datetime.now() - timedelta(days=30)
    # period.month  period.year
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
    result = result.strftime("%d.%m.%Y")
    return result


@register.simple_tag()
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
    result = result.strftime("%d.%m.%Y")
    return result

