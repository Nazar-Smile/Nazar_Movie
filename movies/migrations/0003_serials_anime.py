# Generated by Django 4.1.5 on 2023-01-11 14:18

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_rename_movieshorts_movieshots'),
    ]

    operations = [
        migrations.CreateModel(
            name='Serials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
                ('tagline', models.CharField(default='', max_length=100, verbose_name='Слоган')),
                ('description', models.TextField(verbose_name='Описание')),
                ('poster', models.ImageField(upload_to='serials/', verbose_name='Постер')),
                ('year', models.PositiveBigIntegerField(default=2022, verbose_name='Дата выхода')),
                ('country', models.CharField(max_length=30, verbose_name='Страна')),
                ('world_premiere', models.DateField(default=datetime.date.today, verbose_name='Премьера в мире')),
                ('budget', models.PositiveBigIntegerField(default=0, help_text='Указывать сумму в долларах', verbose_name='Бюджет')),
                ('fees_in_usa', models.PositiveBigIntegerField(default=0, help_text='Указывать сумму в долларах', verbose_name='Сборы в США')),
                ('fees_in_world', models.PositiveBigIntegerField(default=0, help_text='Указывать сумму в долларах', verbose_name='Сборы в мире')),
                ('url', models.SlugField(max_length=130, unique=True)),
                ('draft', models.BooleanField(default=False, verbose_name='Черновик')),
                ('actors', models.ManyToManyField(related_name='serials_actor', to='movies.actor', verbose_name='Актёры')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='movies.category', verbose_name='Категория')),
                ('directors', models.ManyToManyField(related_name='serials_director', to='movies.actor', verbose_name='Режиссер')),
                ('genres', models.ManyToManyField(to='movies.genre', verbose_name='Жанры')),
            ],
            options={
                'verbose_name': 'Сериал',
                'verbose_name_plural': 'Сериалы',
            },
        ),
        migrations.CreateModel(
            name='Anime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
                ('tagline', models.CharField(default='', max_length=100, verbose_name='Слоган')),
                ('description', models.TextField(verbose_name='Описание')),
                ('poster', models.ImageField(upload_to='anime/', verbose_name='Постер')),
                ('year', models.PositiveBigIntegerField(default=2022, verbose_name='Дата выхода')),
                ('country', models.CharField(max_length=30, verbose_name='Страна')),
                ('world_premiere', models.DateField(default=datetime.date.today, verbose_name='Премьера в мире')),
                ('budget', models.PositiveBigIntegerField(default=0, help_text='Указывать сумму в долларах', verbose_name='Бюджет')),
                ('fees_in_usa', models.PositiveBigIntegerField(default=0, help_text='Указывать сумму в долларах', verbose_name='Сборы в США')),
                ('fees_in_world', models.PositiveBigIntegerField(default=0, help_text='Указывать сумму в долларах', verbose_name='Сборы в мире')),
                ('url', models.SlugField(max_length=130, unique=True)),
                ('draft', models.BooleanField(default=False, verbose_name='Черновик')),
                ('actors', models.ManyToManyField(related_name='anime_actor', to='movies.actor', verbose_name='Актёры')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='movies.category', verbose_name='Категория')),
                ('directors', models.ManyToManyField(related_name='anime_director', to='movies.actor', verbose_name='Режиссер')),
                ('genres', models.ManyToManyField(to='movies.genre', verbose_name='Жанры')),
            ],
            options={
                'verbose_name': 'Аниме',
                'verbose_name_plural': 'Аниме',
            },
        ),
    ]