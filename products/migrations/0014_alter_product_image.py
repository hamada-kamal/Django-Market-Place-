# Generated by Django 3.2.6 on 2021-09-26 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0013_auto_20210920_1416'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='', upload_to='prodcut_img/', verbose_name='Change Image'),
            preserve_default=False,
        ),
    ]
