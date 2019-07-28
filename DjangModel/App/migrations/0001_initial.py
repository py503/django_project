# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('p_name', models.CharField(max_length=16, unique=True)),
                ('p_age', models.IntegerField(default=18, db_column='age')),
                ('p_sex', models.BooleanField(default=False, db_column='sex')),
            ],
        ),
    ]
