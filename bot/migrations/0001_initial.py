# Generated by Django 5.0 on 2024-01-29 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Bot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('leverage', models.FloatField()),
                ('order_amount', models.FloatField()),
                ('stop_loss', models.FloatField()),
                ('take_profit', models.FloatField()),
                ('watch_dog', models.FloatField(null=True)),
                ('trade_now', models.BooleanField()),
                ('is_in_process', models.BooleanField(default=True)),
                ('start_date', models.DateTimeField(null=True)),
                ('end_date', models.DateTimeField(null=True)),
                ('asset_list_names', models.ManyToManyField(to='bot.asset')),
            ],
        ),
    ]
