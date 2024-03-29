# Generated by Django 5.0 on 2024-01-29 18:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('strategy', '0002_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Indicator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('type', models.CharField(max_length=16)),
                ('time_frame', models.CharField(max_length=8)),
                ('buy_sell', models.CharField(max_length=16)),
                ('keep_signal', models.IntegerField()),
                ('necessary', models.BooleanField()),
                ('close_str', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='close', to='strategy.strategy')),
                ('open_str', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='open', to='strategy.strategy')),
            ],
        ),
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('long_period', models.IntegerField(null=True)),
                ('consider', models.BooleanField(null=True)),
                ('OHLCV_value', models.CharField(max_length=128, null=True)),
                ('short_period', models.IntegerField(null=True)),
                ('fast_period', models.IntegerField(null=True)),
                ('slow_period', models.IntegerField(null=True)),
                ('signal_period', models.IntegerField(null=True)),
                ('cross', models.CharField(max_length=256, null=True)),
                ('upper_band', models.IntegerField(null=True)),
                ('lower_band', models.IntegerField(null=True)),
                ('rsi_length', models.IntegerField(null=True)),
                ('rsi_type', models.CharField(max_length=32, null=True)),
                ('indicator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='settings', to='indicator.indicator')),
            ],
        ),
    ]
