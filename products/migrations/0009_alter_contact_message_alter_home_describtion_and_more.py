# Generated by Django 4.1.3 on 2022-11-19 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0008_payment_prodref_alter_products_ref"),
    ]

    operations = [
        migrations.AlterField(
            model_name="contact",
            name="message",
            field=models.TextField(max_length=2083),
        ),
        migrations.AlterField(
            model_name="home",
            name="describtion",
            field=models.TextField(max_length=2038),
        ),
        migrations.AlterField(
            model_name="products",
            name="description",
            field=models.TextField(max_length=2083),
        ),
        migrations.AlterField(
            model_name="products",
            name="ref",
            field=models.CharField(
                default="CpLMlT9EvNRrEQ8SIRTHcQgaRV9uOEajysQ1qY3DFKZA9tINnNRngvlsk2le0akgj7k<function uuid4 at 0x00000237BDE65B20>",
                max_length=200,
                unique=True,
            ),
        ),
    ]
