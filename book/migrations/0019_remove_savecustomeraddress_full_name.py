# Generated by Django 2.2.4 on 2019-09-03 10:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0018_auto_20190902_1235'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='savecustomeraddress',
            name='full_name',
        ),
    ]
