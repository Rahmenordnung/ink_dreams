# Generated by Django 2.2.4 on 2019-09-01 23:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0014_order_billing_address'),
    ]

    operations = [
        migrations.RenameField(
            model_name='billingaddress',
            old_name='street_address',
            new_name='house_address',
        ),
    ]