# Generated by Django 3.2.6 on 2021-10-14 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0028_auto_20211014_1509'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=56, unique=True, verbose_name='Product Name'),
        ),
    ]
