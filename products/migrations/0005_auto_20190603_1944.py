# Generated by Django 2.2.1 on 2019-06-03 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20190603_1944'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subcategory',
            name='slug',
            field=models.SlugField(help_text='Заполнится при сохранении', max_length=250, verbose_name='Slug'),
        ),
    ]