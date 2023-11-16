# Generated by Django 4.2.6 on 2023-11-15 11:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crm_app', '0002_alter_quotation_stavka4'),
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=25, unique=True, verbose_name='currency')),
                ('currency_name', models.CharField(choices=[('BYR', 'Беларуский руб.'), ('EU', 'Евро'), ('CNY', 'Китайский юань'), ('RUB', 'российский руб.'), ('USD', 'Доллар США'), ('KZT', 'Казахский тенге'), ('UAG', 'Украинская гривна')], max_length=3)),
            ],
            options={
                'verbose_name': 'Валюта',
                'verbose_name_plural': 'Валюта',
            },
        ),
        migrations.AddField(
            model_name='quotation',
            name='price1',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='quotation',
            name='price2',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='quotation',
            name='price3',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='quotation',
            name='currency1',
            field=models.ForeignKey(blank=True, max_length=3, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='currency1', to='crm_app.currency', verbose_name='Валюта'),
        ),
        migrations.AddField(
            model_name='quotation',
            name='currency2',
            field=models.ForeignKey(blank=True, max_length=3, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='currency2', to='crm_app.currency', verbose_name='Валюта'),
        ),
        migrations.AddField(
            model_name='quotation',
            name='currency3',
            field=models.ForeignKey(blank=True, max_length=3, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='currency3', to='crm_app.currency', verbose_name='Валюта'),
        ),
    ]