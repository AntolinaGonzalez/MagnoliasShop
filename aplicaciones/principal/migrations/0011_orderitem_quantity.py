# Generated by Django 3.0.7 on 2020-07-03 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0010_remove_clothing_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='quantity',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
