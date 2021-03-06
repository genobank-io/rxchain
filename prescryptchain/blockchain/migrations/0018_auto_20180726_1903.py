# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-07-26 19:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blockchain', '0017_auto_20180723_1645'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='medication',
            name='prescription',
        ),
        migrations.RenameField(
            model_name='prescription',
            old_name='rxid',
            new_name='hash_id',
        ),
        migrations.RemoveField(
            model_name='prescription',
            name='bought',
        ),
        migrations.RemoveField(
            model_name='prescription',
            name='details',
        ),
        migrations.RemoveField(
            model_name='prescription',
            name='diagnosis',
        ),
        migrations.RemoveField(
            model_name='prescription',
            name='encrypted_data',
        ),
        migrations.RemoveField(
            model_name='prescription',
            name='extras',
        ),
        migrations.RemoveField(
            model_name='prescription',
            name='medic_cedula',
        ),
        migrations.RemoveField(
            model_name='prescription',
            name='medic_hospital',
        ),
        migrations.RemoveField(
            model_name='prescription',
            name='medic_name',
        ),
        migrations.RemoveField(
            model_name='prescription',
            name='patient_age',
        ),
        migrations.RemoveField(
            model_name='prescription',
            name='patient_name',
        ),
        migrations.DeleteModel(
            name='Medication',
        ),
    ]
