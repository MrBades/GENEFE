# Generated by Django 4.0.3 on 2022-11-16 06:34

from django.db import migrations, models
import products.models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_products_ref'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='ref',
            field=models.CharField(default=products.models.ref_gen, max_length=200, unique=True),
        ),
    ]
