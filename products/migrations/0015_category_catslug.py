# Generated by Django 3.2.6 on 2021-09-29 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0014_alter_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='CATsLug',
            field=models.SlugField(blank=True, null=True, verbose_name='slug'),
        ),
    ]
