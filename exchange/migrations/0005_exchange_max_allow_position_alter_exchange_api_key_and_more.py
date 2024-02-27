# Generated by Django 5.0 on 2024-02-23 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exchange', '0004_remove_exchange_max_allow_position_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='exchange',
            name='max_allow_position',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='exchange',
            name='api_key',
            field=models.CharField(default=1, max_length=128),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='exchange',
            name='secret_key',
            field=models.CharField(default=1, max_length=128),
            preserve_default=False,
        ),
    ]