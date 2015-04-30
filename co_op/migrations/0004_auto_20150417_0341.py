# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('co_op', '0003_posting_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posting',
            name='user',
            field=models.OneToOneField(related_name='user', null=True, to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
