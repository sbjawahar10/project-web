# Generated by Django 5.0.2 on 2024-04-15 03:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0018_remove_cart_total_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='total_price',
        ),
    ]
