# Generated by Django 5.0 on 2024-03-09 15:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0006_rename_market_accounts_bot_exchanges_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bot',
            old_name='exchanges_id',
            new_name='market_accounts',
        ),
    ]
