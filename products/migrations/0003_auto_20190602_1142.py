# Generated by Django 2.2.1 on 2019-06-02 08:42

from django.db import migrations, models
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20190602_1129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='product_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='products.ProductType', verbose_name='Тип товара'),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='product_type', chained_model_field='product_type', on_delete=django.db.models.deletion.CASCADE, related_name='products', to='products.Category', verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='products.ProductType', verbose_name='Тип товара'),
        ),
        migrations.AlterField(
            model_name='product',
            name='subcategory',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='category', chained_model_field='category', on_delete=django.db.models.deletion.CASCADE, related_name='products', to='products.SubCategory', verbose_name='Подкатегория'),
        ),
    ]