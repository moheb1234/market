# Generated by Django 5.0 on 2024-03-16 10:58

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Hire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_type', models.CharField(default='hire', max_length=16)),
                ('name', models.CharField(max_length=64, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('job_title', models.CharField(max_length=64)),
                ('country', models.CharField(max_length=32)),
                ('city', models.CharField(max_length=32)),
                ('cv', models.FileField(upload_to='cv')),
                ('descriptions', models.TextField()),
                ('passport_number', models.ImageField(upload_to='passport_number')),
                ('self_photo', models.ImageField(upload_to='self_photo')),
            ],
        ),
        migrations.CreateModel(
            name='Support',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Signal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_type', models.CharField(default='signal', max_length=16)),
                ('telegram_id', models.CharField(max_length=32)),
                ('time_for_signal', models.CharField(max_length=128)),
                ('favorite_asset_names', models.TextField()),
                ('exchange_names', models.TextField()),
                ('favorite_time_frames', models.TextField()),
                ('rules', models.TextField()),
                ('wallet_amount', models.FloatField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'object_type')},
            },
        ),
    ]
