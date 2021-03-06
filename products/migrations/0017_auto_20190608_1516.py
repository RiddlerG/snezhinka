# Generated by Django 2.2.1 on 2019-06-08 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0016_auto_20190608_1150'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='price',
        ),
        migrations.RemoveField(
            model_name='product',
            name='sale',
        ),
        migrations.AddField(
            model_name='product',
            name='materials',
            field=models.ManyToManyField(related_name='products', to='products.ProductMaterial', verbose_name='Материалы'),
        ),
        migrations.AddField(
            model_name='product',
            name='sizes',
            field=models.ManyToManyField(related_name='products', to='products.ProductSize', verbose_name='Размеры'),
        ),
    ]
