# Generated by Django 4.2.6 on 2023-12-17 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm_app', '0004_alter_documents_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='sdelka',
            name='common_direction',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='Место загрузки'),
        ),
        migrations.AlterField(
            model_name='sdelka',
            name='debitorka1',
            field=models.BooleanField(default=False, verbose_name='подтвержение выгузки1 (дебиторка)'),
        ),
        migrations.AlterField(
            model_name='sdelka',
            name='debitorka10',
            field=models.BooleanField(default=False, verbose_name='подтвержение выгузки10 (дебиторка)'),
        ),
        migrations.AlterField(
            model_name='sdelka',
            name='debitorka2',
            field=models.BooleanField(default=False, verbose_name='подтвержение выгузки2 (дебиторка)'),
        ),
        migrations.AlterField(
            model_name='sdelka',
            name='debitorka3',
            field=models.BooleanField(default=False, verbose_name='подтвержение выгузки3 (дебиторка)'),
        ),
        migrations.AlterField(
            model_name='sdelka',
            name='debitorka4',
            field=models.BooleanField(default=False, verbose_name='подтвержение выгузки4 (дебиторка)'),
        ),
        migrations.AlterField(
            model_name='sdelka',
            name='debitorka5',
            field=models.BooleanField(default=False, verbose_name='подтвержение выгузки5 (дебиторка)'),
        ),
        migrations.AlterField(
            model_name='sdelka',
            name='debitorka6',
            field=models.BooleanField(default=False, verbose_name='подтвержение выгузки6 (дебиторка)'),
        ),
        migrations.AlterField(
            model_name='sdelka',
            name='debitorka7',
            field=models.BooleanField(default=False, verbose_name='подтвержение выгузки7 (дебиторка)'),
        ),
        migrations.AlterField(
            model_name='sdelka',
            name='debitorka8',
            field=models.BooleanField(default=False, verbose_name='подтвержение выгузки8 (дебиторка)'),
        ),
        migrations.AlterField(
            model_name='sdelka',
            name='debitorka9',
            field=models.BooleanField(default=False, verbose_name='подтвержение выгузки9 (дебиторка)'),
        ),
        migrations.AlterField(
            model_name='sdelka',
            name='status_sdelka_other',
            field=models.CharField(blank=True, choices=[('DE-KZ', 'DE-KZ'), ('DE-LV', 'DE-LV'), ('FR-DE', 'FR-DE'), ('BY-PL', 'BY-PL'), ('DE-PL', 'DE-PL'), ('DE-FR', 'DE-FR'), ('FR-BY', 'FR-BY'), ('BY-KZ', 'BY-KZ')], max_length=20, null=True, verbose_name='направление'),
        ),
    ]
