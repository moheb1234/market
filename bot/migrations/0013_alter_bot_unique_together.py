# Generated by Django 5.0 on 2024-03-16 12:08

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0012_alter_bot_strategy'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='bot',
            unique_together={('user', 'name')},
        ),
    ]
