# Generated by Django 3.2.6 on 2021-08-18 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=14, verbose_name='Product Name '),
        ),
    ]
