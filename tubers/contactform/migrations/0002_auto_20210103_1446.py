# Generated by Django 3.1.4 on 2021-01-03 09:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contactform', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactform',
            name='created_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 1, 3, 14, 46, 10, 598900)),
        ),
    ]