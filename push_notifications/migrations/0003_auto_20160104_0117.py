# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('push_notifications', '0002_auto_20151006_1526'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gcmdevice',
            name='device_id',
            field=models.CharField(max_length=60, blank=True, help_text='ANDROID_ID / TelephonyManager.getDeviceId() (always as hex)', null=True, verbose_name='Device ID', db_index=True),
        ),
    ]
