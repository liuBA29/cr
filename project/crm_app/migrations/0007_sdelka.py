# Generated by Django 4.2.6 on 2023-10-30 18:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crm_app', '0006_stavka'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sdelka',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripsion', models.CharField(blank=True, max_length=150, verbose_name='Описание потребності')),
                ('client', models.ForeignKey(max_length=20, on_delete=django.db.models.deletion.CASCADE, to='crm_app.client')),
                ('stavka_from_supplyer', models.ManyToManyField(to='crm_app.stavka')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
