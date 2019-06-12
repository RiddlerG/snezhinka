# Generated by Django 2.2.1 on 2019-06-12 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20190612_0933'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='address',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Улица, дом, квартира / офис'),
        ),
        migrations.AlterField(
            model_name='user',
            name='country',
            field=models.CharField(blank=True, default='Россия', max_length=250, null=True, verbose_name='Страна'),
        ),
        migrations.AlterField(
            model_name='user',
            name='full_name',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='ФИО'),
        ),
        migrations.AlterField(
            model_name='user',
            name='locality',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Город / Населённый пункт'),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Телефон'),
        ),
        migrations.AlterField(
            model_name='user',
            name='postcode',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Индекс'),
        ),
        migrations.AlterField(
            model_name='user',
            name='region',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Регион / Область'),
        ),
    ]
