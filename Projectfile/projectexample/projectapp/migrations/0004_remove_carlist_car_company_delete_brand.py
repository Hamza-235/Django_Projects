# Generated by Django 5.2.2 on 2025-06-15 07:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projectapp', '0003_brand_carlist_car_company'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carlist',
            name='car_company',
        ),
        migrations.DeleteModel(
            name='brand',
        ),
    ]
