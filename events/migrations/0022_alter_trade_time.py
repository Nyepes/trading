# Generated by Django 4.0.6 on 2022-07-24 23:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0021_alter_trade_managers_alter_trade_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trade',
            name='time',
            field=models.TimeField(blank=True, default=datetime.time(23, 52, 29, 548155), verbose_name='Time'),
        ),
    ]