# Generated by Django 2.2.4 on 2019-09-07 21:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0023_auto_20190907_2205'),
    ]

    operations = [
        migrations.RenameField(
            model_name='savecustomeraddress',
            old_name='countries',
            new_name='country',
        ),
    ]
