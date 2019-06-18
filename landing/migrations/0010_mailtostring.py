# Generated by Django 2.2.1 on 2019-06-18 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0009_aboutus_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='MailToString',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=250, verbose_name='E-mail')),
            ],
            options={
                'verbose_name': 'Кому отправлять',
                'verbose_name_plural': 'Кому отправлять',
            },
        ),
    ]