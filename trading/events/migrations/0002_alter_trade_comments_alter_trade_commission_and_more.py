# Generated by Django 4.0.6 on 2022-07-21 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trade',
            name='comments',
            field=models.TextField(blank=True, null=True, verbose_name='Comments'),
        ),
        migrations.AlterField(
            model_name='trade',
            name='commission',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Commission'),
        ),
        migrations.AlterField(
            model_name='trade',
            name='date',
            field=models.DateField(blank=True, verbose_name='Event Date'),
        ),
        migrations.AlterField(
            model_name='trade',
            name='entry_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Entry Price'),
        ),
        migrations.AlterField(
            model_name='trade',
            name='exit_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Exit Price'),
        ),
        migrations.AlterField(
            model_name='trade',
            name='locate_fees',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Locate Fees'),
        ),
        migrations.AlterField(
            model_name='trade',
            name='profit',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Profit'),
        ),
        migrations.AlterField(
            model_name='trade',
            name='shares',
            field=models.IntegerField(blank=True, null=True, verbose_name='Number of Shares'),
        ),
        migrations.AlterField(
            model_name='trade',
            name='stop_loss',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Stop Loss'),
        ),
        migrations.AlterField(
            model_name='trade',
            name='take_profit',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Take Profit'),
        ),
        migrations.AlterField(
            model_name='trade',
            name='ticker',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Ticker'),
        ),
        migrations.AlterField(
            model_name='trade',
            name='time',
            field=models.TimeField(blank=True, verbose_name='Time'),
        ),
        migrations.AlterField(
            model_name='trade',
            name='wl',
            field=models.CharField(blank=True, max_length=2, null=True, verbose_name='W/L'),
        ),
    ]
