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

    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Время последнего обновления')

    class Meta:
        abstract = True


class Transport(models.Model):
    slug = models.SlugField(max_length=25, db_index=True, unique=True, verbose_name='transport')
    transport_name = models.CharField(max_length=15, db_index=True)

    def __str__(self):
        return self.transport_name

    class Meta:
        verbose_name = "Транспорт"
        verbose_name_plural = "Транспорт"


class Direction(models.Model):
    slug = models.SlugField(max_length=25, db_index=True, unique=True, verbose_name='direcrion')
    direction_name = models.CharField(max_length=15, db_index=True)

    def __str__(self):
        return self.direction_name

    class Meta:
        verbose_name = "Направление"
        verbose_name_plural = "Направление"


# ------------------------


class Currency(models.Model):
    slug = models.SlugField(max_length=25, db_index=True, unique=True, verbose_name='currency')
    currency_name = models.CharField(max_length=3, db_index=True)

    def __str__(self):
        return self.currency_name

    class Meta:
        verbose_name = "Валюта"
        verbose_name_plural = "Валюта"


class Client(Contragent):
    client_status = models.BooleanField(default=False, verbose_name="Постоянный клиент")

    class Meta:
        verbose_name = "Заказчик"
        verbose_name_plural = "Заказчики"


    def __str__(self):
        return self.company_name

    def get_absolute_url(self):
        return reverse('show_client', kwargs={'c_id': self.pk})


class Supplyer(Contragent):
    supplyer_status = models.BooleanField(default=False, verbose_name="Надежный перевозчик")

    def __str__(self):
        return self.company_name

    class Meta:
        verbose_name = "Перевозчик"
        verbose_name_plural = "Перевозчики"


    def get_absolute_url(self):
        return reverse('show_supplyer', kwargs={'c_id': self.pk})


class OtherCompany(Contragent):
    descripsion = models.CharField(max_length=150, blank=True, verbose_name='Описание вида деятельности')

    def __str__(self):
        return self.company_name

    class Meta:
        verbose_name = "Сторонняя организация"
        verbose_name_plural = "Сторонние организации"


    def get_absolute_url(self):
        return reverse('show_other_company', kwargs={'c_id': self.pk})


# =================================operations========
class Operation(models.Model):

    class Meta:
        abstract = True


class Sdelka(Operation):
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Время последнего обновления')

    description = models.CharField(max_length=250, blank=True, verbose_name='Описание потребности')
    client = models.ForeignKey(Client, max_length=20, on_delete=models.CASCADE, verbose_name='Заказчик')

    common_transport = models.ForeignKey(Transport, max_length=20, blank=True, null=True, on_delete=models.CASCADE,
                                         verbose_name='Транспорт',
                                         related_name='transport')

    client_price = models.PositiveIntegerField(default=0, verbose_name='Цена')
    client_currency = models.ForeignKey(Currency, max_length=3, blank=True, null=True, on_delete=models.PROTECT,
                                        verbose_name='Валюта', related_name="client_currency")
# supplyer1
    supplyer_1 = models.ForeignKey(Supplyer, max_length=40, blank=True, null=True, on_delete=models.PROTECT,
                                   verbose_name='Перевозчик', related_name="stavka1")
    sup_price_1 = models.PositiveIntegerField(default=0, verbose_name='Цена')
    currency1 = models.ForeignKey(Currency, max_length=3, blank=True, null=True, on_delete=models.PROTECT,
                                  verbose_name='Валюта', related_name="currency1")
    comment_field1 = models.CharField(max_length=280, blank=True, verbose_name='Комментарий Перевозчика')
# supplyer2
    supplyer_2 = models.ForeignKey(Supplyer, max_length=40, blank=True, null=True, on_delete=models.PROTECT,
                                   verbose_name='Перевозчик 2', related_name="stavka2")
    sup_price_2 = models.PositiveIntegerField(default=0, verbose_name='Цена')
    currency2 = models.ForeignKey(Currency, max_length=3, blank=True, null=True, on_delete=models.PROTECT,
                                  verbose_name='Валюта', related_name="currency2")
    comment_field2 = models.CharField(max_length=280, blank=True, verbose_name='Комментарий Перевозчика 2 ')
# supplyer3
    supplyer_3 = models.ForeignKey(Supplyer, max_length=40, blank=True, null=True, on_delete=models.PROTECT,
                                   verbose_name='Перевозчик 3', related_name="stavka3")
    sup_price_3 = models.PositiveIntegerField(default=0, verbose_name='Цена')
    currency3 = models.ForeignKey(Currency, max_length=3, blank=True, null=True, on_delete=models.PROTECT,
                                  verbose_name='Валюта', related_name="currency3")
    comment_field3 = models.CharField(max_length=280, blank=True, verbose_name='Комментарий Перевозчика 3')
# supplyer4
    supplyer_4 = models.ForeignKey(Supplyer, max_length=40, blank=True, null=True, on_delete=models.PROTECT,
                                   verbose_name='Перевозчик 4', related_name="stavka4")
    sup_price_4 = models.PositiveIntegerField(default=0, verbose_name='Цена')
    currency4 = models.ForeignKey(Currency, max_length=3, blank=True, null=True, on_delete=models.PROTECT,
                                  verbose_name='Валюта', related_name="currency4")
    comment_field4 = models.CharField(max_length=280, blank=True, verbose_name='Комментарий Перевозчика 4')
# supplyer5
    supplyer_5 = models.ForeignKey(Supplyer, max_length=40, blank=True, null=True, on_delete=models.PROTECT,
                                   verbose_name='Перевозчик 5', related_name="stavka5")
    sup_price_5 = models.PositiveIntegerField(default=0, verbose_name='Цена')
    currency5 = models.ForeignKey(Currency, max_length=3, blank=True, null=True, on_delete=models.PROTECT,
                                  verbose_name='Валюта', related_name="currency5")
    comment_field5 = models.CharField(max_length=280, blank=True, verbose_name='Комментарий Перевозчика 5')
# supplyer6
    supplyer_6 = models.ForeignKey(Supplyer, max_length=40, blank=True, null=True, on_delete=models.PROTECT,
                                   verbose_name='Перевозчик 6', related_name="stavka6")
    sup_price_6 = models.PositiveIntegerField(default=0, verbose_name='Цена')
    currency6 = models.ForeignKey(Currency, max_length=3, blank=True, null=True, on_delete=models.PROTECT,
                                  verbose_name='Валюта', related_name="currency6")
    comment_field6 = models.CharField(max_length=280, blank=True, verbose_name='Комментарий Перевозчика 6')
# supplyer7
    supplyer_7 = models.ForeignKey(Supplyer, max_length=40, blank=True, null=True, on_delete=models.PROTECT,
                                   verbose_name='Перевозчик 7', related_name="stavka7")
    sup_price_7 = models.PositiveIntegerField(default=0, verbose_name='Цена')
    currency7 = models.ForeignKey(Currency, max_length=3, blank=True, null=True, on_delete=models.PROTECT,
                                  verbose_name='Валюта', related_name="currency7")
    comment_field7 = models.CharField(max_length=280, blank=True, verbose_name='Комментарий Перевозчика 7')
# supplyer8
    supplyer_8 = models.ForeignKey(Supplyer, max_length=40, blank=True, null=True, on_delete=models.PROTECT,
                                   verbose_name='Перевозчик 8', related_name="stavka8")
    sup_price_8 = models.PositiveIntegerField(default=0, verbose_name='Цена')
    currency8 = models.ForeignKey(Currency, max_length=3, blank=True, null=True, on_delete=models.PROTECT,
                                  verbose_name='Валюта', related_name="currency8")
    comment_field8 = models.CharField(max_length=280, blank=True, verbose_name='Комментарий Перевозчика 8')
# supplyer9
    supplyer_9 = models.ForeignKey(Supplyer, max_length=40, blank=True, null=True, on_delete=models.PROTECT,
                                   verbose_name='Перевозчик 9', related_name="stavka9")
    sup_price_9 = models.PositiveIntegerField(default=0, verbose_name='Цена')
    currency9 = models.ForeignKey("Currency", max_length=3, blank=True, null=True, on_delete=models.PROTECT,
                                  verbose_name='Валюта', related_name="currency9")
    comment_field9 = models.CharField(max_length=280, blank=True, verbose_name='Комментарий Перевозчика 9')
# supplyer10
    supplyer_10 = models.ForeignKey(Supplyer, max_length=40, blank=True, null=True, on_delete=models.PROTECT,
                                    verbose_name='Перевозчик 10', related_name="stavka10")
    sup_price_10 = models.PositiveIntegerField(default=0, verbose_name='Цена')
    currency10 = models.ForeignKey("Currency", max_length=3, blank=True, null=True, on_delete=models.PROTECT,
                                   verbose_name='Валюта', related_name="currency10")
    comment_field10 = models.CharField(max_length=280, blank=True, verbose_name='Комментарий Перевозчика 10')

    # new
    number = models.PositiveIntegerField(unique=True, null=True, verbose_name='номер сделки')

    loading_country_1 = models.ForeignKey(Direction, max_length=15, blank=True, null=True, on_delete=models.CASCADE,
                                          verbose_name='Место загрузки', related_name='loading_country_1')
    unloading_country_1 = models.ForeignKey(Direction, max_length=15, blank=True, null=True, on_delete=models.CASCADE,
                                            verbose_name='Место разгрузки', related_name='unloading_country_1')
    loading_country_2 = models.ForeignKey(Direction, max_length=15, blank=True, null=True, on_delete=models.CASCADE,
                                          verbose_name='Место загрузки', related_name='loading_country_2')
    unloading_country_2 = models.ForeignKey(Direction, max_length=15, blank=True, null=True, on_delete=models.CASCADE,
                                            verbose_name='Место разгрузки', related_name='unloading_country_2')
    loading_country_3 = models.ForeignKey(Direction, max_length=15, blank=True, null=True, on_delete=models.CASCADE,
                                          verbose_name='Место загрузки', related_name='loading_country_3')
    unloading_country_3 = models.ForeignKey(Direction, max_length=15, blank=True, null=True, on_delete=models.CASCADE,
                                            verbose_name='Место разгрузки', related_name='unloading_country_3')
    loading_country_4 = models.ForeignKey(Direction, max_length=15, blank=True, null=True, on_delete=models.CASCADE,
                                          verbose_name='Место загрузки', related_name='loading_country_4')
    unloading_country_4 = models.ForeignKey(Direction, max_length=15, blank=True, null=True, on_delete=models.CASCADE,
                                            verbose_name='Место разгрузки', related_name='unloading_country_4')

    loading_country_5 = models.ForeignKey(Direction, max_length=15, blank=True, null=True, on_delete=models.CASCADE,
                                          verbose_name='Место загрузки', related_name='loading_country_5')
    unloading_country_5 = models.ForeignKey(Direction, max_length=15, blank=True, null=True, on_delete=models.CASCADE,
                                            verbose_name='Место разгрузки', related_name='unloading_country_5')
    loading_country_6 = models.ForeignKey(Direction, max_length=15, blank=True, null=True, on_delete=models.CASCADE,
                                          verbose_name='Место загрузки', related_name='loading_country_6')
    unloading_country_6 = models.ForeignKey(Direction, max_length=15, blank=True, null=True, on_delete=models.CASCADE,
                                            verbose_name='Место разгрузки', related_name='unloading_country_6')
    loading_country_7 = models.ForeignKey(Direction, max_length=15, blank=True, null=True, on_delete=models.CASCADE,
                                          verbose_name='Место загрузки', related_name='loading_country_7')
    unloading_country_7 = models.ForeignKey(Direction, max_length=15, blank=True, null=True, on_delete=models.CASCADE,
                                            verbose_name='Место разгрузки', related_name='unloading_country_7')
    loading_country_8 = models.ForeignKey(Direction, max_length=15, blank=True, null=True, on_delete=models.CASCADE,
                                          verbose_name='Место загрузки', related_name='loading_country_8')
    unloading_country_8 = models.ForeignKey(Direction, max_length=15, blank=True, null=True, on_delete=models.CASCADE,
                                            verbose_name='Место разгрузки', related_name='unloading_country_8')
    loading_country_9 = models.ForeignKey(Direction, max_length=15, blank=True, null=True, on_delete=models.CASCADE,
                                          verbose_name='Место загрузки', related_name='loading_country_9')
    unloading_country_9 = models.ForeignKey(Direction, max_length=15, blank=True, null=True, on_delete=models.CASCADE,
                                            verbose_name='Место разгрузки', related_name='unloading_country_9')
    loading_country_10 = models.ForeignKey(Direction, max_length=15, blank=True, null=True, on_delete=models.CASCADE,
                                           verbose_name='Место загрузки', related_name='loading_country_10')
    unloading_country_10 = models.ForeignKey(Direction, max_length=15, blank=True, null=True, on_delete=models.CASCADE,
                                             verbose_name='Место разгрузки', related_name='unloading_country_10')

    data_zagruzki_1 = models.DateField(blank=True,max_length=40,  null=True, verbose_name='Дата загрузки')
    data_vygruzki_1 = models.CharField(blank=True,max_length=40,  null=True, verbose_name='Дата выгрузки')
    data_zagruzki_2 = models.DateField(blank=True,max_length=40,  null=True, verbose_name='Дата загрузки')
    data_vygruzki_2 = models.CharField(blank=True, max_length=40, null=True, verbose_name='Дата выгрузки')
    data_zagruzki_3 = models.DateField(blank=True,max_length=40,  null=True, verbose_name='Дата загрузки')
    data_vygruzki_3 = models.CharField(blank=True,max_length=40,  null=True, verbose_name='Дата выгрузки')
    data_zagruzki_4 = models.DateField(blank=True,max_length=40,  null=True, verbose_name='Дата загрузки')
    data_vygruzki_4 = models.CharField(blank=True, max_length=40, null=True, verbose_name='Дата выгрузки')
    data_zagruzki_5 = models.DateField(blank=True,max_length=40,  null=True, verbose_name='Дата загрузки')
    data_vygruzki_5 = models.CharField(blank=True,max_length=40,  null=True, verbose_name='Дата выгрузки')
    data_zagruzki_6 = models.DateField(blank=True,max_length=40,  null=True, verbose_name='Дата загрузки')
    data_vygruzki_6 = models.CharField(blank=True,max_length=40,  null=True, verbose_name='Дата выгрузки')
    data_zagruzki_7 = models.DateField(blank=True,max_length=40,  null=True, verbose_name='Дата загрузки')
    data_vygruzki_7 = models.CharField(blank=True,max_length=40,  null=True, verbose_name='Дата выгрузки')
    data_zagruzki_8 = models.DateField(blank=True,max_length=40,  null=True, verbose_name='Дата загрузки')
    data_vygruzki_8 = models.CharField(blank=True,max_length=40,  null=True, verbose_name='Дата выгрузки')
    data_zagruzki_9 = models.DateField(blank=True,max_length=40,  null=True, verbose_name='Дата загрузки')
    data_vygruzki_9 = models.CharField(blank=True,max_length=40,  null=True, verbose_name='Дата выгрузки')
    data_zagruzki_10 = models.DateField(blank=True, max_length=40, null=True, verbose_name='Дата загрузки')
    data_vygruzki_10 = models.CharField(blank=True,max_length=40,  null=True, verbose_name='Дата выгрузки')

    STATUS_SDELKA_CHOICES = [
        ('PROJECT', 'Проект'),
        ('CURRENT', 'Текущая'),
        ('CLOSED', 'Закрыта'),
    ]

    STATUS_SDELKA_OTHER_CHOICES = [
        ('NEW', 'Новая'),
        ('TAKEN', 'Принята'),
        ('ON_WAY', 'В пути'),
        ('UPLOADED', 'Выгружена'),

    ]

    status_sdelka = models.CharField(max_length=20, default='Проект', choices=STATUS_SDELKA_CHOICES,
                                     verbose_name='Статус общий сделки')
    status_sdelka_other = models.CharField(max_length=20, default='Новая', choices=STATUS_SDELKA_OTHER_CHOICES,
                                           verbose_name='Статус состояния сделки')

    debitorka1 = models.BooleanField(default=False, verbose_name='подтвержение выгузки1')
    debitorka2 = models.BooleanField(default=False, verbose_name='подтвержение выгузки2')
    debitorka3 = models.BooleanField(default=False, verbose_name='подтвержение выгузки3')
    debitorka4 = models.BooleanField(default=False, verbose_name='подтвержение выгузки4')
    debitorka5 = models.BooleanField(default=False, verbose_name='подтвержение выгузки5')
    debitorka6 = models.BooleanField(default=False, verbose_name='подтвержение выгузки6')
    debitorka7 = models.BooleanField(default=False, verbose_name='подтвержение выгузки7')
    debitorka8 = models.BooleanField(default=False, verbose_name='подтвержение выгузки8')
    debitorka9 = models.BooleanField(default=False, verbose_name='подтвержение выгузки9')
    debitorka10 = models.BooleanField(default=False, verbose_name='подтвержение выгузки10')

    profit = models.CharField(max_length=20, blank=True, verbose_name='прибыль в евро')
    class Meta:
        ordering = ['-time_update', '-time_create', 'number',]

    def __str__(self):
        return 'Сделка №' +  str(self.number)

    def get_absolute_url(self):
        return reverse('show_sdelka', kwargs={'c_id': self.pk})


# ===================доки=====
class Documents(models.Model):
    name = models.CharField(max_length=35, blank=True, null=True, verbose_name='Название документа')
    sdelka = models.ForeignKey(Sdelka, on_delete=models.CASCADE, blank=True, null=True,
                               verbose_name="Документы в сделке")
    client = models.ForeignKey(Client, on_delete=models.CASCADE, blank=True, null=True,
                               verbose_name="Документы от заказчика")
    supplyer = models.ForeignKey(Supplyer, on_delete=models.CASCADE, blank=True, null=True,
                                 verbose_name="Документы от перевозчика")
    other_company = models.ForeignKey(OtherCompany, on_delete=models.CASCADE, blank=True, null=True,
                                           verbose_name="Документы прочие")
    DOC_CHOICES = [
        ('Договор', 'Договор'),
        ('ТН', 'ТН'),
        ('Коносамент', 'Коносамент'),
        ('Дебиторка', 'Дебиторка'),
        ('Корпоративные', 'Корпоративные'),

    ]
    type = models.CharField(max_length=35, default='Договор', choices=DOC_CHOICES,
                                     verbose_name ='Вид документа')
    file = models.FileField(null=True, blank=True)

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse('show_document', kwargs={'c_id': self.pk})



# =======================================
class Quotation(Operation):
    STATUS_CHOICES = [
        ('NEW', 'Новая'),
        ('CURRENT', 'В работе'),
        ('CLOSED', 'Закрыта'),

    ]

    RESULT_CHOICES = [
        ('NOT_READY', 'Груз не готов'),
        ('PRICE_GOOD', 'Прошли по цене'),
        ('PRICE_BAD', 'Не прошли по цене'),

    ]
    description = models.CharField(max_length=250, blank=True, verbose_name='Описание потребности')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Время последнего обновления')
    client = models.ForeignKey(Client, max_length=20, on_delete=models.CASCADE,
                               verbose_name='Заказчик', related_name="qu_client")

    loading_country = models.ForeignKey(Direction, max_length=15, blank=True, null=True, on_delete=models.CASCADE,
                                        verbose_name='Место загрузки',
                                        related_name='common_loading_country')
    unloading_country = models.ForeignKey(Direction, max_length=15, blank=True, null=True, on_delete=models.CASCADE,
                                          verbose_name='Место выгрузки',
                                          related_name='common_unloading_country')

    common_transport = models.ForeignKey(Transport, max_length=20, blank=True, null=True, on_delete=models.CASCADE,
                                         verbose_name='Транспорт',
                                         related_name='com_transport')


###

    #####


    supplyer_1 = models.ForeignKey(Supplyer, max_length=40, blank=True, null=True, on_delete=models.PROTECT,
                                   verbose_name='Перевозчик', related_name="supplyer_1")
    sup_price_1 = models.PositiveIntegerField(default=0, verbose_name='Цена')
    currency1 = models.ForeignKey(Currency, max_length=3, blank=True, null=True, on_delete=models.PROTECT,
                                  verbose_name='Валюта', related_name="qu_currency1")
    comment_field1 = models.CharField(max_length=280, blank=True, verbose_name='Комментарий к ставке 1')

    supplyer_2 = models.ForeignKey(Supplyer, max_length=40, blank=True, null=True, on_delete=models.PROTECT,
                                   verbose_name='Перевозчик 2', related_name="supplyer_2")
    sup_price_2 = models.PositiveIntegerField(default=0, verbose_name='Цена')
    currency2 = models.ForeignKey(Currency, max_length=3, blank=True, null=True, on_delete=models.PROTECT,
                                  verbose_name='Валюта', related_name="qu_currency2")
    comment_field2 = models.CharField(max_length=280, blank=True, verbose_name='Комментарий к ставке ')

    supplyer_3 = models.ForeignKey(Supplyer, max_length=40, blank=True, null=True, on_delete=models.PROTECT,
                                   verbose_name='Перевозчик 3', related_name="supplyer_3")
    sup_price_3 = models.PositiveIntegerField(default=0, verbose_name='Цена')
    currency3 = models.ForeignKey(Currency, max_length=3, blank=True, null=True, on_delete=models.PROTECT,
                                  verbose_name='Валюта', related_name="qu_currency3")
    comment_field3 = models.CharField(max_length=280, blank=True, verbose_name='Комментарий к ставке 3')

    supplyer_4 = models.ForeignKey(Supplyer, max_length=40, blank=True, null=True, on_delete=models.PROTECT,
                                   verbose_name='Перевозчик 4', related_name="supplyer_4")
    sup_price_4 = models.PositiveIntegerField(default=0, verbose_name='Цена')
    currency4 = models.ForeignKey(Currency, max_length=3, blank=True, null=True, on_delete=models.PROTECT,
                                  verbose_name='Валюта', related_name="qu_currency4")
    comment_field4 = models.CharField(max_length=280, blank=True, verbose_name='Комментарий к ставке4')

    supplyer_5 = models.ForeignKey(Supplyer, max_length=40, blank=True, null=True, on_delete=models.PROTECT,
                                   verbose_name='Перевозчик 5', related_name="supplyer_5")
    sup_price_5 = models.PositiveIntegerField(default=0, verbose_name='Цена')
    currency5 = models.ForeignKey(Currency, max_length=3, blank=True, null=True, on_delete=models.PROTECT,
                                  verbose_name='Валюта', related_name="qu_currency5")
    comment_field5 = models.CharField(max_length=280, blank=True, verbose_name='Комментарий к ставке 5')

    supplyer_6 = models.ForeignKey(Supplyer, max_length=40, blank=True, null=True, on_delete=models.PROTECT,
                                   verbose_name='Перевозчик 6', related_name="supplyer_6")
    sup_price_6 = models.PositiveIntegerField(default=0, verbose_name='Цена')
    currency6 = models.ForeignKey(Currency, max_length=3, blank=True, null=True, on_delete=models.PROTECT,
                                  verbose_name='Валюта', related_name="qu_currency6")
    comment_field6 = models.CharField(max_length=280, blank=True, verbose_name='Комментарий к ставке 6')

    supplyer_7 = models.ForeignKey(Supplyer, max_length=40, blank=True, null=True, on_delete=models.PROTECT,
                                   verbose_name='Перевозчик 7', related_name="supplyer_7")
    sup_price_7 = models.PositiveIntegerField(default=0, verbose_name='Цена')
    currency7 = models.ForeignKey(Currency, max_length=3, blank=True, null=True, on_delete=models.PROTECT,
                                  verbose_name='Валюта', related_name="qu_currency7")
    comment_field7 = models.CharField(max_length=280, blank=True, verbose_name='Комментарий к ставке 7')

    supplyer_8 = models.ForeignKey(Supplyer, max_length=40, blank=True, null=True, on_delete=models.PROTECT,
                                   verbose_name='Перевозчик 8', related_name="supplyer_8")
    sup_price_8 = models.PositiveIntegerField(default=0, verbose_name='Цена')
    currency8 = models.ForeignKey(Currency, max_length=3, blank=True, null=True, on_delete=models.PROTECT,
                                  verbose_name='Валюта', related_name="qu_currency8")
    comment_field8 = models.CharField(max_length=280, blank=True, verbose_name='Комментарий к ставке 8')

    supplyer_9 = models.ForeignKey(Supplyer, max_length=40, blank=True, null=True, on_delete=models.PROTECT,
                                   verbose_name='Перевозчик 9', related_name="supplyer_9")
    sup_price_9 = models.PositiveIntegerField(default=0, verbose_name='Цена')
    currency9 = models.ForeignKey("Currency", max_length=3, blank=True, null=True, on_delete=models.PROTECT,
                                  verbose_name='Валюта', related_name="qu_currency9")
    comment_field9 = models.CharField(max_length=280, blank=True, verbose_name='Комментарий к ставке 9')

    supplyer_10 = models.ForeignKey(Supplyer, max_length=40, blank=True, null=True, on_delete=models.PROTECT,
                                    verbose_name='Перевозчик 10', related_name="supplyer_10")
    sup_price_10 = models.PositiveIntegerField(default=0, verbose_name='Цена')
    currency10 = models.ForeignKey("Currency", max_length=3, blank=True, null=True, on_delete=models.PROTECT,
                                   verbose_name='Валюта', related_name="qu_currency10")



    comment_field1 = models.CharField(max_length=280, blank=True, verbose_name='Комментарий к ставке 1')
    comment_field2 = models.CharField(max_length=280, blank=True, verbose_name='Комментарий к ставке ')
    comment_field3 = models.CharField(max_length=280, blank=True, verbose_name='Комментарий к ставке 3')
    comment_field4 = models.CharField(max_length=280, blank=True, verbose_name='Комментарий к ставке 4')
    comment_field5 = models.CharField(max_length=280, blank=True, verbose_name='Комментарий к ставке 5')
    comment_field6 = models.CharField(max_length=280, blank=True, verbose_name='Комментарий к ставке 6')
    comment_field7 = models.CharField(max_length=280, blank=True, verbose_name='Комментарий к ставке 7')
    comment_field8 = models.CharField(max_length=280, blank=True, verbose_name='Комментарий к ставке 8')
    comment_field9 = models.CharField(max_length=280, blank=True, verbose_name='Комментарий к ставке 9')
    comment_field10 = models.CharField(max_length=280, blank=True, verbose_name='Комментарий к ставке 10')

    status = models.CharField(max_length=20, default='Новая', choices=STATUS_CHOICES, verbose_name='Статус')

    result = models.CharField(max_length=20, blank=True, null=True, choices=RESULT_CHOICES, verbose_name='Результат')

    def get_absolute_url(self):
        return reverse('show_quotation', kwargs={'c_id': self.pk})

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = "Котировка"
        verbose_name_plural = "Котировки"








