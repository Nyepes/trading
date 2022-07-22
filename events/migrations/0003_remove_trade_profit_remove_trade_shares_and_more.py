# Generated by Django 4.0.6 on 2022-07-22 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_alter_trade_comments_alter_trade_commission_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trade',
            name='profit',
        ),
        migrations.RemoveField(
            model_name='trade',
            name='shares',
        ),
        migrations.RemoveField(
            model_name='trade',
            name='take_profit',
        ),
        migrations.RemoveField(
            model_name='trade',
            name='wl',
        ),
        migrations.AddField(
            model_name='trade',
            name='trade_type',
            field=models.CharField(blank=True, max_length=2, null=True, verbose_name='Trade Type'),
        ),
    ]
