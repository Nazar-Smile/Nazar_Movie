# Generated by Django 4.1.5 on 2023-01-12 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_serials_anime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anime',
            name='year',
            field=models.PositiveBigIntegerField(default=2023, verbose_name='Дата выхода'),
        ),
    ]