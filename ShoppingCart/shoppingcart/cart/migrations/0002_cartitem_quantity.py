# Generated by Django 5.0.2 on 2024-02-12 12:05

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("cart", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="cartitem",
            name="quantity",
            field=models.IntegerField(default="123"),
            preserve_default=False,
        ),
    ]
