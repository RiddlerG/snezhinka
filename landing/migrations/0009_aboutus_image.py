# Generated by Django 2.2.1 on 2019-06-16 07:01

from django.db import migrations, models
import landing.models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0008_remove_aboutus_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutus',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=landing.models.AboutUs.get_picture_url, verbose_name='Изображение'),
        ),
    ]
