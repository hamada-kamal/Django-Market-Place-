# Generated by Django 3.2.6 on 2021-08-13 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Product Name ')),
                ('image', models.ImageField(blank=True, null=True, upload_to='prodcut_img/', verbose_name='Image')),
                ('price', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Price')),
                ('digital', models.BooleanField(blank=True, default=False, null=True)),
                ('discription', models.TextField(blank=True, max_length=200, null=True)),
                ('PRDSLug', models.SlugField(blank=True, null=True, verbose_name='slug')),
                ('like', models.ManyToManyField(blank=True, to='products.Customer')),
            ],
        ),
    ]