# Generated by Django 2.0.4 on 2018-05-08 01:58

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pcmapp', '0011_auto_20180420_0435'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_reg_no', models.CharField(max_length=20)),
                ('car_model', models.CharField(max_length=20)),
                ('car_engine_chasis', models.CharField(max_length=20)),
                ('car_primary_sec', models.BinaryField(choices=[('1', 'Primary'), ('2', 'Secondary')], max_length=1)),
                ('Car_status', models.BooleanField()),
            ],
        ),
        migrations.RenameField(
            model_name='member',
            old_name='member_car_model',
            new_name='member_phone',
        ),
        migrations.RemoveField(
            model_name='member',
            name='member_car_no',
        ),
        migrations.RemoveField(
            model_name='member',
            name='member_engine_chasis',
        ),
        migrations.RemoveField(
            model_name='member',
            name='member_status',
        ),
        migrations.RemoveField(
            model_name='member',
            name='member_tel_no',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='member',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='member_expiry_date',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='payment_receipt_date',
        ),
        migrations.AddField(
            model_name='member',
            name='member_address_postcode',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='member',
            name='member_address_state',
            field=models.CharField(blank=True, choices=[('JH', 'Johor'), ('KH', 'Kedah'), ('KN', 'Kelantan'), ('KL', 'Kuala Lumpur'), ('LA', 'Labuan'), ('ME', 'Melaka'), ('NS', 'Negeri Sembilan'), ('PH', 'Pahang'), ('PK', 'Perak'), ('PL', 'Perlis'), ('PG', 'Pulau Pinang'), ('PJ', 'Putrajaya'), ('SA', 'Sabah'), ('SK', 'Sarawak'), ('SL', 'Selangor'), ('TE', 'Terengganu')], max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='member',
            name='member_birthdate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='member',
            name='member_on_chat',
            field=models.BinaryField(choices=[('1', 'YES'), ('0', 'NO')], max_length=1, null=True),
        ),
        migrations.AddField(
            model_name='member',
            name='member_source',
            field=models.CharField(blank=True, choices=[('FB', 'Facebook'), ('TW', 'Twitter'), ('SC', 'Service center'), ('IN', 'Instagram'), ('RE', 'Referal'), ('WO', 'Word of mouth'), ('OT', 'Other')], max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='payment',
            name='payment_date',
            field=models.DateField(blank=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='payment',
            name='payment_receipt_image',
            field=models.FileField(default=1, upload_to='uploadreceipt'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='payment',
            name='payment_type',
            field=models.CharField(choices=[('1', 'New'), ('2', 'Renewal'), ('3', 'Supplementary')], default=1, max_length=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='member',
            name='member_email',
            field=models.EmailField(max_length=200),
        ),
        migrations.AlterField(
            model_name='member',
            name='member_expiry_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='member_since',
            field=models.DateField(),
        ),
        migrations.AddField(
            model_name='car',
            name='car_member_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pcmapp.Member'),
        ),
        migrations.AddField(
            model_name='payment',
            name='payment_car_reg_no',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='pcmapp.Car'),
            preserve_default=False,
        ),
    ]
