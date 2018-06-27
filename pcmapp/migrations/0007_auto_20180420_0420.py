# Generated by Django 2.0.4 on 2018-04-20 04:20

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('pcmapp', '0006_auto_20180420_0418'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='member_expiry_date',
            field=models.DateField(blank=True, default=datetime.datetime(2018, 4, 20, 4, 20, 34, 180334, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='member',
            name='member_since',
            field=models.DateField(blank=True, default=datetime.datetime(2018, 4, 20, 4, 20, 34, 180158, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='member',
            name='member_status',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]