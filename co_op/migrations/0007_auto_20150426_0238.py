# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('co_op', '0006_auto_20150426_0224'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='user',
        ),
        migrations.AlterField(
            model_name='posting',
            name='user_profile',
            field=models.ForeignKey(related_name='profile', to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
