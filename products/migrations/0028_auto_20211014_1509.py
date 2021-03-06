# Generated by Django 3.2.6 on 2021-10-14 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0027_rename_mobile_customer_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='discription_ar',
            field=models.TextField(blank=True, max_length=200, null=True, verbose_name='Description'),
        ),
        migrations.AddField(
            model_name='product',
            name='name_ar',
            field=models.CharField(default='', max_length=56, verbose_name='Product Name'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='customer',
            name='phone',
            field=models.CharField(blank=True, max_length=11, null=True, verbose_name='Mobile'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=56, verbose_name='Product Name'),
        ),
    ]
