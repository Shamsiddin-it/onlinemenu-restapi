# Generated by Django 5.0 on 2024-11-20 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlinemenu', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='total_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8),
        ),
    ]
