# Generated by Django 4.2.6 on 2023-12-26 21:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm_app', '0008_qfilter'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='qfilter',
            options={'ordering': ['qfilter']},
        ),
        migrations.RenameField(
            model_name='qfilter',
            old_name='filter',
            new_name='qfilter',
        ),
    ]
