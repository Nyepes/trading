# Generated by Django 4.0.6 on 2022-07-24 05:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('events', '0003_remove_trade_profit_remove_trade_shares_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trade',
            name='trade_type',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Trade Type'),
        ),
        migrations.CreateModel(
            name='PageUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('initial_equity', models.DecimalField(blank=True, decimal_places=2, max_digits=10, verbose_name='Initial Equity')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='trade',
            name='page_user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.PROTECT, to='events.pageuser'),
        ),
    ]