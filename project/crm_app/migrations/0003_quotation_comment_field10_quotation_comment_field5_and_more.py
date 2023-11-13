# Generated by Django 4.2.6 on 2023-11-13 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm_app', '0002_alter_quotation_comment_field4_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='quotation',
            name='comment_field10',
            field=models.CharField(blank=True, max_length=280, verbose_name='комментарий к ставке 10'),
        ),
        migrations.AddField(
            model_name='quotation',
            name='comment_field5',
            field=models.CharField(blank=True, max_length=280, verbose_name='комментарий к ставке 5'),
        ),
        migrations.AddField(
            model_name='quotation',
            name='comment_field6',
            field=models.CharField(blank=True, max_length=280, verbose_name='комментарий к ставке 6'),
        ),
        migrations.AddField(
            model_name='quotation',
            name='comment_field7',
            field=models.CharField(blank=True, max_length=280, verbose_name='комментарий к ставке 7'),
        ),
        migrations.AddField(
            model_name='quotation',
            name='comment_field8',
            field=models.CharField(blank=True, max_length=280, verbose_name='комментарий к ставке 8'),
        ),
        migrations.AddField(
            model_name='quotation',
            name='comment_field9',
            field=models.CharField(blank=True, max_length=280, verbose_name='комментарий к ставке 9'),
        ),
        migrations.AddField(
            model_name='quotation',
            name='stavka10',
            field=models.CharField(blank=True, max_length=20, verbose_name='ставка 10'),
        ),
        migrations.AddField(
            model_name='quotation',
            name='stavka5',
            field=models.CharField(blank=True, max_length=20, verbose_name='ставка 5'),
        ),
        migrations.AddField(
            model_name='quotation',
            name='stavka6',
            field=models.CharField(blank=True, max_length=20, verbose_name='ставка 6'),
        ),
        migrations.AddField(
            model_name='quotation',
            name='stavka7',
            field=models.CharField(blank=True, max_length=20, verbose_name='ставка 7'),
        ),
        migrations.AddField(
            model_name='quotation',
            name='stavka8',
            field=models.CharField(blank=True, max_length=20, verbose_name='ставка 8'),
        ),
        migrations.AddField(
            model_name='quotation',
            name='stavka9',
            field=models.CharField(blank=True, max_length=20, verbose_name='ставка 9'),
        ),
        migrations.AlterField(
            model_name='quotation',
            name='comment_field1',
            field=models.CharField(blank=True, max_length=280, verbose_name='комментарий к ставке 1'),
        ),
        migrations.AlterField(
            model_name='quotation',
            name='comment_field2',
            field=models.CharField(blank=True, max_length=280, verbose_name='комментарий к ставке '),
        ),
        migrations.AlterField(
            model_name='quotation',
            name='comment_field3',
            field=models.CharField(blank=True, max_length=280, verbose_name='комментарий к ставке 3'),
        ),
        migrations.AlterField(
            model_name='quotation',
            name='comment_field4',
            field=models.CharField(blank=True, max_length=280, verbose_name='комментарий к ставке4'),
        ),
        migrations.AlterField(
            model_name='quotation',
            name='stavka3',
            field=models.CharField(blank=True, max_length=20, verbose_name='ставка 3'),
        ),
    ]
