# Generated by Django 5.2.2 on 2025-06-22 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectapp', '0008_carlist_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='carlist',
            name='model_id',
            field=models.IntegerField(default=None),
        ),
    ]
