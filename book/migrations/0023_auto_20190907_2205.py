# Generated by Django 2.2.4 on 2019-09-07 21:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0022_book_cover'),
    ]

    operations = [
        migrations.RenameField(
            model_name='savecustomeraddress',
            old_name='country',
            new_name='countries',
        ),
    ]
