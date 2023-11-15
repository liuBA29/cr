from django.core.validators import MinValueValidator
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

    def get_absolute_url(self):
        return reverse('show_client', kwargs={'c_id':self.pk})

class Supplyer(Contragent):
    supplyer_status = models.BooleanField(default=False, verbose_name="Надежный перевозчик")

    def __str__(self):
        return self.company_name

    class Meta:
        verbose_name= "Перевозчик"
        verbose_name_plural = "Перевозчики"
        ordering = ['created']

    def get_absolute_url(self):
        return reverse('show_supplyer', kwargs={'c_id': self.pk})

class OtherCompany(Contragent):
    descripsion = models.CharField(max_length=150, blank=True, verbose_name='Описание вида деятельности')

    def __str__(self):
        return self.company_name

    class Meta:
        verbose_name="Сторонняя организация"
        verbose_name_plural = "Сторонние организации"
        ordering = ['created']

    def get_absolute_url(self):
        return reverse('show_other_company', kwargs={'c_id':self.pk})

#=================================operations========
class Operation(models.Model):
     descripsion = models.CharField(max_length=150, blank=True, verbose_name='Описание потребності')
     transport = models.CharField(default='avto', max_length=20)



     class Meta:
        abstract = True







class Sdelka(Operation):
    client = models.ForeignKey(Client, max_length=20,blank = True, on_delete=models.CASCADE, verbose_name='Заказчик')

    cl_price = models.CharField(max_length=20, default=1, verbose_name='цена заказчика')
    cl_currency = models.CharField(max_length=20, default='eu', verbose_name='валюта заказчика')

    supplyer1 = models.ForeignKey(Supplyer, max_length=20,  blank = True, on_delete=models.CASCADE, verbose_name='Перевозчик1', related_name='Перевозчик1')
    sup_price1 = models.CharField(max_length=20, blank=True,verbose_name='цена перевозчіка1')
    sup_currency1 = models.CharField(max_length=20, blank=True,verbose_name='валюта перевозчіка1')
    sup_pometka1 = models.CharField(max_length=20,blank=True, verbose_name='пометка перевозчіка1')

    supplyer2 = models.ForeignKey(Supplyer, max_length=20, blank = True, on_delete=models.CASCADE, verbose_name='Перевозчик2', related_name='Перевозчик2' )
    sup_price2 = models.CharField(max_length=20, blank=True, verbose_name='цена перевозчіка2')
    sup_currency2 = models.CharField(max_length=20, blank=True, verbose_name='валюта перевозчіка2')
    sup_pometka2 = models.CharField(max_length=20, blank=True, verbose_name='пометка перевозчіка2')


    common_direction=models.CharField(max_length=20, blank = True, verbose_name='общее направленіе доставкі')
    common_transport = models.CharField(max_length=20, blank = True, verbose_name='транспорт іспользуемый в сделке')
    profit = models.CharField(max_length=20, blank=True, verbose_name='прібыль в евро')

    cl_documents = models.CharField(max_length=20, blank=True, verbose_name='документы заказчіка')

    sup_documents1 = models.CharField(max_length=20, blank=True, verbose_name='документы перевозчика1')
    sup_documents2 = models.CharField(max_length=20, blank=True, verbose_name='документы перевозчика2')

    data_zagruzki_1 = models.CharField(max_length=20,blank=True, verbose_name='дата загрузки1')
    data_vygruzki_1 = models.CharField(max_length=20, blank=True, verbose_name='дата выгрузки1')

    data_zagruzki_2 = models.CharField(max_length=20, blank=True, verbose_name='дата загрузки2')
    data_vygruzki_2 = models.CharField(max_length=20, blank=True, verbose_name='дата выгрузки2')

    debitorks = models.BooleanField(default=False,  verbose_name='подтвержение выгузки1')
    debitorka2 = models.BooleanField(default=False, verbose_name='подтвержение выгузки2')

    status = models.CharField(max_length=20, blank = True, verbose_name='статус: текущие, закрытые, проект')
    status_other = models.CharField(max_length=20, blank = True, verbose_name='статус other- новая, принята, в пути, выгружена')
    number = models.CharField(max_length=20, blank = True, verbose_name='номер сделки')

    def __str__(self):
        return 'Сделка с клиентом:' + str(self.client)


    def get_absolute_url(self):
        return reverse('show_operation', kwargs={'c_id':self.pk})


class Currency(models.Model):

    slug = models.SlugField(max_length=25, db_index=True, unique=True, verbose_name='currency')
    currency_name = models.CharField(max_length=3,  db_index=True)
    def __str__(self):
        return self.currency_name

    class Meta:
        verbose_name = "Валюта"
        verbose_name_plural = "Валюта"


class Quotation(Operation):
    descripsion = models.CharField(max_length=250, blank = True, verbose_name='Описание потребности')
    client = models.ForeignKey(Client, max_length=20, on_delete=models.CASCADE, verbose_name='Заказчик')
    common_direction = models.CharField(max_length=20, blank = True, verbose_name='Направление доставки')
    common_transport = models.CharField(max_length=20, blank=True, verbose_name='Транспорт')



    stavka1 = models.ForeignKey(Supplyer, max_length=40, blank=True, null=True, on_delete=models.PROTECT, verbose_name='Перевозчик', related_name="stavka1")
    price1 = models.PositiveIntegerField(default=0, verbose_name='Цена')
    currency1 = models.ForeignKey(Currency, max_length=3, blank=True, null=True, on_delete=models.PROTECT,
                                  verbose_name='Валюта', related_name="currency1")
    comment_field1=  models.CharField(max_length=280,blank = True,  verbose_name='Комментарий к ставке 1')

    stavka2 = models.ForeignKey(Supplyer, max_length=40, blank=True, null=True, on_delete=models.PROTECT, verbose_name='Перевозчик 2', related_name="stavka2")
    price2 = models.PositiveIntegerField(default=0, verbose_name='Цена')
    currency2 = models.ForeignKey(Currency, max_length=3, blank=True, null=True, on_delete=models.PROTECT,
                                  verbose_name='Валюта', related_name="currency2")
    comment_field2= models.CharField(max_length=280, blank = True, verbose_name='Комментарий к ставке ')

    stavka3 = models.ForeignKey(Supplyer, max_length=40, blank=True,null=True, on_delete=models.PROTECT, verbose_name='Перевозчик 3', related_name="stavka3")
    price3 = models.PositiveIntegerField(default=0, verbose_name='Цена')
    currency3 = models.ForeignKey(Currency, max_length=3, blank=True, null=True, on_delete=models.PROTECT,
                                  verbose_name='Валюта', related_name="currency3")
    comment_field3 = models.CharField(max_length=280, blank = True, verbose_name='Комментарий к ставке 3')

    stavka4 = models.ForeignKey(Supplyer, max_length=40, blank=True, null=True, on_delete=models.PROTECT, verbose_name='Перевозчик 4', related_name="stavka4")
    price4 = models.PositiveIntegerField(default=0, verbose_name='Цена')
    currency4 = models.ForeignKey(Currency, max_length=3, blank=True, null=True, on_delete=models.PROTECT,
                                  verbose_name='Валюта', related_name="currency4")
    comment_field4 = models.CharField(max_length=280, blank = True,verbose_name='Комментарий к ставке4')

    stavka5 = models.ForeignKey(Supplyer, max_length=40, blank=True, null=True, on_delete=models.PROTECT, verbose_name='Перевозчик 5', related_name="stavka5")
    price5 = models.PositiveIntegerField(default=0, verbose_name='Цена')
    currency5 = models.ForeignKey(Currency, max_length=3, blank=True, null=True, on_delete=models.PROTECT,
                                  verbose_name='Валюта', related_name="currency5")
    comment_field5 = models.CharField(max_length=280, blank=True, verbose_name='Комментарий к ставке 5')

    stavka6 = models.ForeignKey(Supplyer, max_length=40, blank=True, null=True, on_delete=models.PROTECT, verbose_name='Перевозчик 6', related_name="stavka6")
    price6 = models.PositiveIntegerField(default=0, verbose_name='Цена')
    currency6 = models.ForeignKey(Currency, max_length=3, blank=True, null=True, on_delete=models.PROTECT,
                                  verbose_name='Валюта', related_name="currency6")
    comment_field6 = models.CharField(max_length=280, blank=True, verbose_name='Комментарий к ставке 6')

    stavka7 = models.ForeignKey(Supplyer, max_length=40, blank=True,null=True, on_delete=models.PROTECT, verbose_name='Перевозчик 7', related_name="stavka7")
    price7 = models.PositiveIntegerField(default=0, verbose_name='Цена')
    currency7 = models.ForeignKey(Currency, max_length=3, blank=True, null=True, on_delete=models.PROTECT,
                                  verbose_name='Валюта', related_name="currency7")
    comment_field7 = models.CharField(max_length=280, blank=True, verbose_name='Комментарий к ставке 7')

    stavka8 = models.ForeignKey(Supplyer, max_length=40, blank=True, null=True, on_delete=models.PROTECT, verbose_name='Перевозчик 8', related_name="stavka8")
    price8 = models.PositiveIntegerField(default=0, verbose_name='Цена')
    currency8 = models.ForeignKey(Currency, max_length=3, blank=True, null=True, on_delete=models.PROTECT,
                                  verbose_name='Валюта', related_name="currency8")
    comment_field8 = models.CharField(max_length=280, blank=True, verbose_name='Комментарий к ставке 8')

    stavka9 = models.ForeignKey(Supplyer, max_length=40, blank=True, null=True, on_delete=models.PROTECT, verbose_name='Перевозчик 9', related_name="stavka9")
    price9 = models.PositiveIntegerField(default=0, verbose_name='Цена')
    currency9 = models.ForeignKey(Currency, max_length=3, blank=True, null=True, on_delete=models.PROTECT,
                                  verbose_name='Валюта', related_name="currency9")
    comment_field9 = models.CharField(max_length=280, blank=True, verbose_name='Комментарий к ставке 9')

    stavka10 = models.ForeignKey(Supplyer, max_length=40, blank=True, null=True, on_delete=models.PROTECT, verbose_name='Перевозчик 10', related_name="stavka10")
    price10 = models.PositiveIntegerField(default=0, verbose_name='Цена')
    currency10 = models.ForeignKey(Currency, max_length=3, blank=True, null=True, on_delete=models.PROTECT,
                                  verbose_name='Валюта', related_name="currency10")
    comment_field10 = models.CharField(max_length=280, blank=True, verbose_name='Комментарий к ставке 10')

    status = models.CharField(max_length=20, default='новая', verbose_name='Статус: новая, в работе, закрыта')

    result = models.CharField(max_length=20, default='не прошли', verbose_name='Результат: прошли по цене, груз не готов, не прошли по цене')


    def get_absolute_url(self):
        return reverse('show_quotation', kwargs={'c_id':self.pk})


    class Meta:
        verbose_name = "Котировка"
        verbose_name_plural = "Котировки"
