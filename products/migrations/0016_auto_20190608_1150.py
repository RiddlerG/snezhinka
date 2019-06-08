# Generated by Django 2.2.1 on 2019-06-08 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0015_product_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price_without_sale',
            field=models.PositiveIntegerField(default=0, verbose_name='Цена без скидки'),
        ),
        migrations.AddField(
            model_name='product',
            name='sale',
            field=models.PositiveIntegerField(default=0, verbose_name='Скидка'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.PositiveIntegerField(default=0, help_text='Заполнится при сохранении', verbose_name='Цена со скидкой'),
        ),
    ]
