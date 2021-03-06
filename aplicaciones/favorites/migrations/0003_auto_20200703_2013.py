# Generated by Django 3.0.7 on 2020-07-03 20:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('principal', '0008_order_orderitem'),
        ('favorites', '0002_auto_20200629_1931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favorito',
            name='objecto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favoritos', to='principal.Clothing'),
        ),
        migrations.AlterField(
            model_name='favorito',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favoritos', to=settings.AUTH_USER_MODEL),
        ),
    ]
