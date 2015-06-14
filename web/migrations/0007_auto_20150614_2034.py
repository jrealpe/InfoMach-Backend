# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0006_auto_20150614_1710'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='content',
            options={'verbose_name': 'Contenido', 'verbose_name_plural': 'Contenidos'},
        ),
        migrations.AlterModelOptions(
            name='contribution',
            options={'verbose_name': 'Contribucion', 'verbose_name_plural': 'Contribuciones'},
        ),
        migrations.AlterModelOptions(
            name='profile',
            options={'verbose_name': 'Perfil', 'verbose_name_plural': 'Perfiles'},
        ),
        migrations.AddField(
            model_name='contribution',
            name='title',
            field=models.CharField(default=b'', max_length=128),
        ),
    ]
