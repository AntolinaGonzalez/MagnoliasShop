# Generated by Django 3.0.7 on 2020-07-03 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0013_orderitem_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]
