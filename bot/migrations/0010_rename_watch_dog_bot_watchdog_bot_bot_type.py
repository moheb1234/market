# Generated by Django 5.0 on 2024-03-13 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0009_alter_asset_bot'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bot',
            old_name='watch_dog',
            new_name='watchdog',
        ),
        migrations.AddField(
            model_name='bot',
            name='bot_type',
            field=models.CharField(default=1, max_length=16),
            preserve_default=False,
        ),
    ]