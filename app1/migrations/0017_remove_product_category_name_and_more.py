# Generated by Django 5.0.2 on 2024-04-11 11:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0016_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='category_name',
        ),
        migrations.RemoveField(
            model_name='product',
            name='subcategory_name',
        ),
    ]