# Generated by Django 5.0 on 2024-02-02 09:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('package', '0003_remove_package_trade_history_package_automate_manual_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='package',
            name='discount_code',
        ),
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=16, unique=True)),
                ('percent', models.IntegerField()),
                ('descriptions', models.CharField(max_length=256, null=True)),
                ('created_date', models.DateField(auto_now_add=True)),
                ('period_validity', models.IntegerField(null=True)),
                ('package', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dicounts', to='package.package')),
            ],
        ),
    ]
