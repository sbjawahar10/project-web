# Generated by Django 5.0.2 on 2024-05-07 01:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0022_wishlist'),
    ]

    operations = [
        migrations.CreateModel(
            name='feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('message', models.CharField(max_length=50)),
            ],
        ),
    ]