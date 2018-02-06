# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grants', '0015_merge'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='hidden_until_scored',
            field=models.BooleanField(default=False),
        ),
    ]
