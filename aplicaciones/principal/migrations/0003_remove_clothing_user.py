# Generated by Django 3.0.7 on 2020-06-27 00:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0002_auto_20200627_0038'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clothing',
            name='user',
        ),
    ]
