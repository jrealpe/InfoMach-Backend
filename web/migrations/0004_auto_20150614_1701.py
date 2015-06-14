# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('web', '0003_auto_20150614_1653'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='user',
            field=models.ForeignKey(default=b'1', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='contribution',
            name='user',
            field=models.ForeignKey(to='web.Profile'),
        ),
    ]
