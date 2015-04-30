# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('co_op', '0002_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='posting',
            name='user',
            field=models.OneToOneField(related_name='user', default=None, to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]