# Generated by Django 3.2 on 2021-08-09 15:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flaskapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='date',
            field=models.DateTimeField(default=datetime.datetime.today),
        ),
    ]
