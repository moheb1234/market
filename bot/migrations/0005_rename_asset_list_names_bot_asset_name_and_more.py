# Generated by Django 5.0 on 2024-03-09 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0004_bot_trade_market'),
        ('exchange', '0005_exchange_max_allow_position_alter_exchange_api_key_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bot',
            old_name='asset_list_names',
            new_name='asset_name',
        ),
        migrations.RemoveField(
            model_name='bot',
            name='exchange',
        ),
        migrations.RemoveField(
            model_name='bot',
            name='is_in_process',
        ),
        migrations.RemoveField(
            model_name='bot',
            name='trade_now',
        ),
        migrations.AddField(
            model_name='asset',
            name='classification',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='asset',
            name='leverage',
            field=models.IntegerField(default=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='asset',
            name='order_amount',
            field=models.FloatField(default=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='asset',
            name='trade_market',
            field=models.CharField(default=2, max_length=32),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bot',
            name='classification',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='bot',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='bot',
            name='image',
            field=models.TextField(default=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bot',
            name='market_accounts',
            field=models.ManyToManyField(to='exchange.exchange'),
        ),
        migrations.AddField(
            model_name='bot',
            name='max_open_position_after_trend',
            field=models.FloatField(default=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bot',
            name='order_timeout',
            field=models.CharField(default=2, max_length=64),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bot',
            name='order_type',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='bot',
            name='spread',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='bot',
            name='end_date',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='bot',
            name='leverage',
            field=models.FloatField(default=20, null=True),
        ),
        migrations.AlterField(
            model_name='bot',
            name='order_amount',
            field=models.FloatField(default=30, null=True),
        ),
        migrations.AlterField(
            model_name='bot',
            name='start_date',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='bot',
            name='take_profit',
            field=models.FloatField(default=5, null=True),
        ),
        migrations.AlterField(
            model_name='bot',
            name='trade_market',
            field=models.CharField(default=2, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='bot',
            name='watch_dog',
            field=models.FloatField(default=5, null=True),
        ),
    ]
