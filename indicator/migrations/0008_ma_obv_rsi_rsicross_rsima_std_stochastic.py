# Generated by Django 5.0 on 2024-02-25 17:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('indicator', '0007_alter_macd_consider_alter_macd_cross'),
    ]

    operations = [
        migrations.CreateModel(
            name='MA',
            fields=[
                ('setting_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='indicator.setting')),
                ('ohlcv_value', models.CharField(default='close', max_length=16)),
                ('ma_type', models.CharField(default='EMA', max_length=32)),
                ('ma_sizes', models.CharField(max_length=128)),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('indicator.setting',),
        ),
        migrations.CreateModel(
            name='OBV',
            fields=[
                ('setting_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='indicator.setting')),
                ('ma_type_obv', models.CharField(default='EMA', max_length=32)),
                ('length', models.IntegerField(default=5)),
                ('cross_with_zero', models.BooleanField(default=True)),
                ('ma_type', models.CharField(default='EMA', max_length=32, null=True)),
                ('ma_length', models.IntegerField(default=14, null=True)),
                ('cross', models.CharField(max_length=128, null=True)),
                ('consider', models.BooleanField(default=False, null=True)),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('indicator.setting',),
        ),
        migrations.CreateModel(
            name='RSI',
            fields=[
                ('setting_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='indicator.setting')),
                ('ohlcv_value', models.CharField(default='close', max_length=16)),
                ('rsi_length', models.IntegerField(default=14)),
                ('signal_upper_band', models.IntegerField(default=70)),
                ('signal_lower_band', models.IntegerField(default=30)),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('indicator.setting',),
        ),
        migrations.CreateModel(
            name='RSICross',
            fields=[
                ('setting_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='indicator.setting')),
                ('ohlcv_value', models.CharField(default='close', max_length=16)),
                ('rsi_length', models.IntegerField(default=14)),
                ('signal_upper_grater', models.IntegerField(default=70)),
                ('signal_lower_less', models.IntegerField(default=30)),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('indicator.setting',),
        ),
        migrations.CreateModel(
            name='RSIMa',
            fields=[
                ('setting_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='indicator.setting')),
                ('ohlcv_value', models.CharField(default='close', max_length=16)),
                ('rsi_length', models.IntegerField(default=14)),
                ('signal_upper_band', models.IntegerField(default=70)),
                ('signal_lower_band', models.IntegerField(default=30)),
                ('ma_type', models.CharField(default='EMA', max_length=32)),
                ('ma_length', models.IntegerField(default=14)),
                ('cross', models.CharField(max_length=128)),
                ('consider', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('indicator.setting',),
        ),
        migrations.CreateModel(
            name='STD',
            fields=[
                ('setting_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='indicator.setting')),
                ('ohlcv_value', models.CharField(default='close', max_length=16)),
                ('length', models.IntegerField(default=20)),
                ('callback', models.IntegerField(default=100)),
                ('price_percent', models.IntegerField(default=60)),
                ('ma_type', models.CharField(default='EMA', max_length=32, null=True)),
                ('ma_length', models.IntegerField(default=14, null=True)),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('indicator.setting',),
        ),
        migrations.CreateModel(
            name='Stochastic',
            fields=[
                ('setting_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='indicator.setting')),
                ('k_length', models.IntegerField(default=14)),
                ('k_smooth', models.IntegerField(default=3)),
                ('d_smooth', models.IntegerField(default=7)),
                ('signal_upper_band', models.IntegerField(default=80)),
                ('signal_lower_band', models.IntegerField(default=20)),
                ('consider', models.BooleanField(default=False)),
                ('cross_k_d', models.BooleanField(default=False)),
                ('for_buy_lower_upper', models.CharField(max_length=128)),
                ('for_buy_lower', models.CharField(max_length=128)),
                ('for_sell_lower_upper', models.CharField(max_length=128)),
                ('for_sell_upper', models.CharField(max_length=128)),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('indicator.setting',),
        ),
    ]