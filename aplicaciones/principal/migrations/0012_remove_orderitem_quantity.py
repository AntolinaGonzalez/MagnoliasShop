# Generated by Django 3.0.7 on 2020-07-03 22:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0011_orderitem_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='quantity',
        ),
    ]
