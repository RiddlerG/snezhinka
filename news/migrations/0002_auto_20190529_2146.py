# Generated by Django 2.2.1 on 2019-05-29 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='slug',
            field=models.SlugField(help_text='Заполнится при сохранении', max_length=250, unique=True, verbose_name='Slug'),
        ),
    ]
