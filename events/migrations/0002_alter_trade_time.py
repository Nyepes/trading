# Generated by Django 4.0.6 on 2022-07-25 06:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trade',
            name='time',
            field=models.TimeField(blank=True, default=datetime.time(6, 17, 29, 404282), verbose_name='Time'),
        ),
    ]