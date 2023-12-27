# Generated by Django 4.2.6 on 2023-12-26 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm_app', '0007_alter_timeperiod_options_timeperiod_created'),
    ]

    operations = [
        migrations.CreateModel(
            name='Qfilter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Время создания')),
                ('filter', models.CharField(max_length=35)),
            ],
            options={
                'ordering': ['filter'],
            },
        ),
    ]
