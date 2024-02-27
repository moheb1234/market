# Generated by Django 5.0 on 2024-02-22 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('strategy', '0003_alter_strategy_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='strategy',
            name='low_high_price',
            field=models.IntegerField(default=5),
        ),
        migrations.AlterField(
            model_name='strategy',
            name='max_price_allow',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='strategy',
            name='min_price_allow',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='strategy',
            name='min_sig_for_close',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='strategy',
            name='min_sig_for_open',
            field=models.IntegerField(default=0),
        ),
    ]