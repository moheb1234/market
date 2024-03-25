# Generated by Django 5.0 on 2024-03-24 17:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('bot', '0013_alter_bot_unique_together'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asset_name', models.CharField(max_length=32)),
                ('position_side', models.CharField(max_length=32)),
                ('open_time', models.DateTimeField()),
                ('close_time', models.DateTimeField()),
                ('entry_price', models.FloatField()),
                ('qty', models.FloatField()),
                ('closed_by', models.CharField(max_length=16)),
                ('income', models.FloatField()),
                ('profit', models.FloatField()),
                ('loss', models.FloatField()),
                ('turnover', models.FloatField()),
                ('bot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bot.bot')),
            ],
        ),
    ]
