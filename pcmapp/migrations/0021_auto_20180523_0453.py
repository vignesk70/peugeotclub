# Generated by Django 2.0.4 on 2018-05-23 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pcmapp', '0020_auto_20180523_0452'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='car_primary_sec',
            field=models.SmallIntegerField(blank=True, choices=[('1', 'Primary'), ('2', 'Secondary')], null=True),
        ),
    ]