# Generated by Django 4.2.6 on 2023-12-15 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm_app', '0003_rename_other_organization_documents_other_company_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documents',
            name='type',
            field=models.CharField(choices=[('Договор', 'Договор'), ('ТН', 'ТН'), ('Коносамент', 'Коносамент'), ('Дебиторка', 'Дебиторка'), ('Корпоративные', 'Корпоративные')], default='Договор', max_length=35, verbose_name='Вид документа'),
        ),
    ]