# Generated by Django 2.2.1 on 2019-06-16 03:54

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0024_product_is_new'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='sale',
            field=models.PositiveIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(100)], verbose_name='Скидка'),
        ),
    ]