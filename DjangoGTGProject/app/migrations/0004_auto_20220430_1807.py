# Generated by Django 2.2.28 on 2022-04-30 16:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20220430_1802'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 30, 18, 7, 54, 433213)),
        ),
    ]