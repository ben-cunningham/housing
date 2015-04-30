# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('address', models.CharField(max_length=50)),
                ('postal_code', models.CharField(max_length=6)),
                ('apartment_number', models.IntegerField(max_length=4)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rent_per_month', models.IntegerField(default=0)),
                ('number_of_rooms', models.IntegerField(default=1)),
                ('number_of_bathrooms', models.IntegerField(default=1)),
                ('average_cost_utilities', models.IntegerField(default=0)),
                ('number_of_roommates', models.IntegerField(default=0)),
                ('address', models.OneToOneField(null=True, to='co_op.Address')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('photo', models.ImageField(upload_to=b'photos/')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Posting',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=150)),
                ('description', models.CharField(max_length=500)),
                ('number_of_semesters', models.IntegerField(default=0)),
                ('house', models.OneToOneField(null=True, to='co_op.House')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='image',
            name='posting',
            field=models.ForeignKey(related_name='images', to='co_op.Posting'),
            preserve_default=True,
        ),
    ]
