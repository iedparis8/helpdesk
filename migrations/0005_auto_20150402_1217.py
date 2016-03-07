# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('helpdesk', '0004_initial_data_import'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usersettings',
            name='user',
            field=models.OneToOneField(related_name='helpdesk_user_settings', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
