# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0003_auto_20160320_2028'),
    ]

    operations = [
        migrations.RenameField(
            model_name='authenticator',
            old_name='date_created',
            new_name='datecreated',
        ),
    ]
