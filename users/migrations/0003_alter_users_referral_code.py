# Generated by Django 5.0 on 2024-03-12 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_remove_users_answer_remove_users_birthday_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='referral_code',
            field=models.IntegerField(null=True),
        ),
    ]
