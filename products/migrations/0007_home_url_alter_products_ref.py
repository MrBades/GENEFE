# Generated by Django 4.0.3 on 2022-11-16 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_home_alter_products_ref'),
    ]

    operations = [
        migrations.AddField(
            model_name='home',
            name='url',
            field=models.CharField(default=1, max_length=2083),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='products',
            name='ref',
            field=models.CharField(default='P9791_VcbXpB1HbFkMLHkzJykjsJ4UI38aCrItS7IKQxGKSyMGYIY-tIFwRdpk4BLaI<function uuid4 at 0x0000023B217EA3A0>', max_length=200, unique=True),
        ),
    ]
