# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_auto_20150614_1648'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='link_video',
            field=models.CharField(max_length=128, null=True, blank=True),
        ),
    ]
