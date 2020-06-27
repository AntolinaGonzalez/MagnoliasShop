# Generated by Django 3.0.7 on 2020-06-27 13:55

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('principal', '0003_remove_clothing_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clothing',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='favorite', to=settings.AUTH_USER_MODEL),
        ),
    ]
