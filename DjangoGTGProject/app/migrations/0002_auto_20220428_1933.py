# Generated by Django 2.2.28 on 2022-04-28 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='price',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='drink',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
