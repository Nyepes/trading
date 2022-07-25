# Generated by Django 4.0.6 on 2022-07-24 23:11

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0016_trade_equity_at_time_alter_trade_page_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trade',
            name='page_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='events.profile'),
        ),
        migrations.AlterField(
            model_name='trade',
            name='time',
            field=models.TimeField(blank=True, default=datetime.time(23, 11, 19, 122691), verbose_name='Time'),
        ),
    ]
