# Generated by Django 2.2.28 on 2022-04-30 16:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20220428_1933'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='order_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 30, 18, 2, 59, 152162)),
        ),
        migrations.AlterField(
            model_name='order',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
