# Generated by Django 2.2.4 on 2019-08-30 12:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_auto_20190830_1225'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='category',
            field=models.CharField(choices=[('FT', 'Fairy Tale'), ('BA', 'Biography/Autobiography'), ('CL', 'Classic'), ('RO', 'Romance'), ('AA', 'Action and Adventure'), ('CD', 'Crime and Detective'), ('CN', 'Comic and Graphic Novel'), ('HI', 'Historical Fiction'), ('MY', 'Mythology'), ('ST', 'Suspense/Thriller'), ('SF', 'Science Fiction'), ('F', 'Fantasy'), ('P', 'Poetry'), ('S', 'Satire'), ('E', 'Essay')], default=django.utils.timezone.now, max_length=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='sticker',
            field=models.CharField(choices=[('P', 'deep-purple'), ('BG', 'blue-grey'), ('E', 'elegant'), ('PK', 'pink'), ('Y', 'yellow'), ('U', 'unique'), ('B', 'brown'), ('A', 'amber'), ('MC', 'mdb-color'), ('DO', 'deep-orange'), ('LG', 'light-green'), ('DG', 'dark-green'), ('C', 'cyan'), ('I', 'indigo'), ('Lb', 'light-blue')], default=django.utils.timezone.now, max_length=2),
            preserve_default=False,
        ),
    ]