# Generated by Django 5.1.7 on 2025-04-04 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0002_remove_itemshopping_quantity_itemshopping_marketname'),
    ]

    operations = [
        migrations.AddField(
            model_name='list',
            name='listName',
            field=models.CharField(default='', max_length=30),
        ),
    ]
