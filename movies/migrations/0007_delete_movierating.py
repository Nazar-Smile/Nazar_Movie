# Generated by Django 4.1.6 on 2023-02-23 17:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0006_movierating'),
    ]

    operations = [
        migrations.DeleteModel(
            name='MovieRating',
        ),
    ]