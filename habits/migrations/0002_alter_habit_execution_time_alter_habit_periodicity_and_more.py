# Generated by Django 5.1.5 on 2025-02-06 13:41

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='habit',
            name='execution_time',
            field=models.PositiveIntegerField(default=0, verbose_name='Время выполнения (в секундах)'),
        ),
        migrations.AlterField(
            model_name='habit',
            name='periodicity',
            field=models.PositiveIntegerField(default=1, verbose_name='Периодичность в днях'),
        ),
        migrations.AlterField(
            model_name='habit',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE,
                                    to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
    ]
