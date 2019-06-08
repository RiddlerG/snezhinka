# Generated by Django 2.2.1 on 2019-06-08 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_auto_20190608_1325'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status_delivery',
            field=models.CharField(choices=[('shipped', 'Отгружено'), ('not_shipped', 'Неотгружено')], default='not_shipped', max_length=250, verbose_name='Статус доставки'),
        ),
        migrations.AddField(
            model_name='order',
            name='status_payment',
            field=models.CharField(choices=[('paid', 'Оплачено'), ('not_paid', 'Неоплачено')], default='not_paid', max_length=250, verbose_name='Статус оплаты'),
        ),
    ]