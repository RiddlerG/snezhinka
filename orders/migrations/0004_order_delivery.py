# Generated by Django 2.2.1 on 2019-06-08 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_auto_20190608_1311'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='delivery',
            field=models.CharField(blank=True, choices=[('Audio', (('vinyl', 'Vinyl'), ('cd', 'CD'))), ('Video', (('vhs', 'VHS Tape'), ('dvd', 'DVD'))), ('unknown', 'Unknown')], max_length=250, null=True, verbose_name='Способ получения товара'),
        ),
    ]
