# Generated by Django 3.2.4 on 2021-06-05 23:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_productindex'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productindex',
            name='anons_ru',
        ),
        migrations.RemoveField(
            model_name='productindex',
            name='anons_uz',
        ),
    ]
