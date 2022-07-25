# Generated by Django 4.0.6 on 2022-07-24 06:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_profile_alter_trade_page_user_delete_person'),
    ]

    operations = [
        migrations.CreateModel(
            name='A',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, verbose_name='Event Date')),
                ('time', models.TimeField(blank=True, verbose_name='Time')),
                ('ticker', models.CharField(blank=True, max_length=10, null=True, verbose_name='Ticker')),
                ('entry_price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Entry Price')),
                ('stop_loss', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Stop Loss')),
                ('locate_fees', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Locate Fees')),
                ('exit_price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Exit Price')),
                ('commission', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Commission')),
                ('trade_type', models.CharField(blank=True, max_length=30, null=True, verbose_name='Trade Type')),
                ('text', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='events.profile')),
            ],
        ),
    ]