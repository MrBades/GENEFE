# Generated by Django 4.0.3 on 2022-11-16 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_products_ref'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='ref',
            field=models.CharField(default='iDygc_WM6ouNNnvotz_QVYPKCxXftl-kaghqcPQjyxmB1ZfX0s8RwEXqFejwHukAS9Y', max_length=200, unique=True),
        ),
    ]
