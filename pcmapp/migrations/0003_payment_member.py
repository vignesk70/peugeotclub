# Generated by Django 2.0.4 on 2018-04-13 05:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pcmapp', '0002_auto_20180413_0508'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='member',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='pcmapp.Member'),
            preserve_default=False,
        ),
    ]