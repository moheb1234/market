# Generated by Django 5.0 on 2024-03-05 10:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_news_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='news',
            old_name=' publishedAt',
            new_name='publishedAt',
        ),
    ]
