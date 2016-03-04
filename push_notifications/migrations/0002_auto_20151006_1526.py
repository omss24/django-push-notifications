# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('push_notifications', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apnsdevice',
            name='user',
            field=models.ForeignKey(blank=True, to='consultant.ConsultantToken', null=True),
        ),
        migrations.AlterField(
            model_name='gcmdevice',
            name='user',
            field=models.ForeignKey(blank=True, to='consultant.ConsultantToken', null=True),
        ),
    ]
