# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Three', '0002_grade'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stu',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('s_name', models.CharField(max_length=16)),
                ('s_age', models.IntegerField(default=1)),
                ('s_grade', models.ForeignKey(to='Three.Grade')),
            ],
        ),
    ]
