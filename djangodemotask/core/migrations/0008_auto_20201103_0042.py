# Generated by Django 3.0.7 on 2020-11-03 00:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0007_auto_20201103_0031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answer', to=settings.AUTH_USER_MODEL),
        ),
    ]
