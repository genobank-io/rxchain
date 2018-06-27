# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-05-08 22:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blockchain', '0015_auto_20180328_1704'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medication',
            name='presentation',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='prescription',
            name='details',
            field=models.TextField(blank=True, default=b''),
        ),
        migrations.AlterField(
            model_name='prescription',
            name='extras',
            field=models.TextField(blank=True, default=b''),
        ),
        migrations.AlterField(
            model_name='prescription',
            name='location',
            field=models.TextField(blank=True, default=b''),
        ),
        migrations.AlterField(
            model_name='prescription',
            name='medic_cedula',
            field=models.TextField(blank=True, default=b''),
        ),
        migrations.AlterField(
            model_name='prescription',
            name='medic_hospital',
            field=models.TextField(blank=True, default=b''),
        ),
        migrations.AlterField(
            model_name='prescription',
            name='medic_name',
            field=models.TextField(blank=True, default=b''),
        ),
        migrations.AlterField(
            model_name='prescription',
            name='patient_age',
            field=models.TextField(blank=True, default=b''),
        ),
        migrations.AlterField(
            model_name='prescription',
            name='patient_name',
            field=models.TextField(blank=True, default=b''),
        ),
        migrations.AlterField(
            model_name='prescription',
            name='previous_hash',
            field=models.TextField(blank=True, default=b''),
        ),
        migrations.AlterField(
            model_name='prescription',
            name='private_key',
            field=models.TextField(blank=True, default=b''),
        ),
        migrations.AlterField(
            model_name='prescription',
            name='public_key',
            field=models.TextField(blank=True, default=b''),
        ),
        migrations.AlterField(
            model_name='prescription',
            name='rxid',
            field=models.TextField(blank=True, default=b''),
        ),
        migrations.AlterField(
            model_name='prescription',
            name='signature',
            field=models.TextField(blank=True, default=b'', null=True),
        ),
    ]