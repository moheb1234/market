# Generated by Django 5.0 on 2024-02-06 12:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('package', '0004_remove_package_discount_code_discount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discount',
            name='package',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='discounts', to='package.package'),
        ),
    ]
