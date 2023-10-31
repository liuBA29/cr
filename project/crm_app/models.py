
from django.db import models
from django.db import models
from django.urls import reverse


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



class Client(Contragent):
    client_status = models.BooleanField(default=False, verbose_name="Постоянный клиент")
    class Meta:
        verbose_name = "Заказчик"
        verbose_name_plural = "Заказчики"
        ordering = ['created']

    def __str__(self):
        return self.company_name

class Supplyer(Contragent):
    supplyer_status = models.BooleanField(default=False, verbose_name="Надежный перевозчик")

    def __str__(self):
        return self.company_name

    class Meta:
        verbose_name= "Перевозчик"
        verbose_name_plural = "Перевозчики"
        ordering = ['created']

    def get_absolute_url(self):
        return reverse('quot', kwargs={'quot_id': self.pk})


class OtherCompany(Contragent):
    descripsion = models.CharField(max_length=150, blank=True, verbose_name='Описание вида деятельности')

    def __str__(self):
        return self.company_name

    class Meta:
        verbose_name="Сторонняя организация"
        verbose_name_plural = "Сторонние организации"
        ordering = ['created']


#=================================operations========
class Operation(models.Model):
    # transport
    # direction
    # description

    class Meta:
        abstract = True





class Stavka(models.Model):
    supplyer = models.ForeignKey(Supplyer, max_length=20, on_delete=models.CASCADE)
    transport = models.CharField(max_length=20)
    direction = models.CharField(max_length=20)
    description = models.CharField(max_length=20)
    price = models.FloatField()

    def __str__(self):
        return str(self.supplyer) + " : " + str(self.price)



class Sdelka(Operation):
    descripsion = models.CharField(max_length=150, blank=True, verbose_name='Описание потребності')
    client = models.ForeignKey(Client, max_length=20, on_delete=models.CASCADE)
    stavka_from_supplyer = models.ManyToManyField(Stavka)