# Generated by Django 2.2.4 on 2019-08-31 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0007_book_discount_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='description',
            field=models.TextField(default='no description provided'),
            preserve_default=False,
        ),
    ]
