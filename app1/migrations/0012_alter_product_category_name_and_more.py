# Generated by Django 5.0.2 on 2024-03-18 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0011_category_product_category_name_subcategory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category_name',
            field=models.CharField(max_length=300),
        ),
        migrations.RemoveField(
            model_name='subcategory',
            name='category',
        ),
        migrations.AddField(
            model_name='product',
            name='subcategory_name',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='category',
        ),
        migrations.DeleteModel(
            name='subcategory',
        ),
    ]