# Generated by Django 5.0 on 2024-03-09 12:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0005_rename_asset_list_names_bot_asset_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bot',
            old_name='market_accounts',
            new_name='exchanges_id',
        ),
    ]