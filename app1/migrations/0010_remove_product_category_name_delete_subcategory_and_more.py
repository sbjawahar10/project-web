# Generated by Django 5.0.2 on 2024-03-15 04:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0009_product_category_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='category_name',
        ),
        migrations.DeleteModel(
            name='Subcategory',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
