# Generated by Django 2.2.1 on 2019-06-06 16:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0013_auto_20190606_1841'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='price',
        ),
        migrations.RemoveField(
            model_name='product',
            name='price_without_sale',
        ),
    ]
