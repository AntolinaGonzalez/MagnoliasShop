# Generated by Django 3.0.7 on 2020-07-03 20:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0009_clothing_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clothing',
            name='slug',
        ),
    ]
