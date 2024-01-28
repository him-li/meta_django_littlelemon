# Generated by Django 4.2.7 on 2024-01-28 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LittleLemonAPI', '0002_category_menuitem_order_orderitem_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='reservation_date',
            field=models.DateTimeField(default=0),
        ),
        migrations.AddField(
            model_name='booking',
            name='reservation_slot',
            field=models.SmallIntegerField(default=10),
        ),
    ]
