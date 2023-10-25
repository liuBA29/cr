
from django.db import models
from django.db import models



class Contragent(models.Model):
    company_name = models.CharField(max_length=35)
    contact_name = models.CharField(max_length=100, blank=True, verbose_name='Контактное лицо')
    email = models.EmailField(max_length=35)
    phone = models.CharField(max_length=30)
    address = models.CharField(max_length=150)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, verbose_name='Время последнего обновления')

    class Meta:
        abstract = True
#------------------------

class Money(models.Model):
    CURRENCY_CHOICES = (
        ('EUR', 'EUR'),
        ('USD', 'USD'),
        ('UAH', 'UAH'),
        ('BYR', 'BYR'),
        ('KZT', 'KZT'),
        ('RUB', 'RUB'),
        ('CNY', 'CNY'),
        ('INR', 'INR'),
    )
    CURRENCY_DEFAULT = 'EUR'

    price = models.FloatField()
    currency = models.CharField(choices=CURRENCY_CHOICES, default=CURRENCY_DEFAULT)

    class Meta:
        verbose_name="Деньги"
        verbose_name_plural="Деньги"

class Stavka(models.Model):
    supplyer = models.ForeignKey('Supplyer', on_delete=models.PROTECT)
    price = models.ForeignKey(Money, on_delete=models.CASCADE)

    # comment_from_supplyer
    # our_comment
    RESULT_CHOICES = (
        ('not ready', 'Груз не готов'),
        ('refused', 'Не прошли по цене'),
        ('allowed', 'Прошли по цене'),
    )
    result = models.CharField(choices=RESULT_CHOICES, default='not ready')
    class Meta:
        verbose_name="Ставка"
        verbose_name_plural="Ставки"


class Client(Contragent):
    client_status = models.BooleanField(default=False, verbose_name="Постоянный клиент")
    class Meta:
        verbose_name="Заказчики"
        verbose_name_plural="Перевозчики"
        ordering = ['created']

    def __str__(self):
        return self.company_name

class Supplyer(Contragent):
    supplyer_status = models.BooleanField(default=False, verbose_name="Надежный перевозчик")

    def __str__(self):
        return self.company_name

    class Meta:
        verbose_name="Перевозчики"
        verbose_name_plural="Перевозчики"
        ordering = ['created']

class OtherCompany(Contragent):
    descripsion = models.CharField(max_length=150, blank=True, verbose_name='Описание вида деятельности')

    def __str__(self):
        return self.company_name

    class Meta:
        verbose_name="Сторонние организации"
        verbose_name_plural = "Сторонние организации"
        ordering = ['created']

class Operation(models.Model):
    # transport
    # direction
    # description

    class Meta:
        abstract = True



