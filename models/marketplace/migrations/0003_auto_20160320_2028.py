# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0002_auto_20160320_1944'),
    ]

    operations = [
        migrations.RenameField(
            model_name='authenticator',
            old_name='user_id',
            new_name='userid',
        ),
    ]
