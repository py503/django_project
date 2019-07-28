# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GoodsTest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('status', models.SmallIntegerField(verbose_name='商品信息', default=1, choices=[(0, '下架'), (1, '上架')])),
                ('detail', tinymce.models.HTMLField(verbose_name='商品详情')),
            ],
        ),
    ]
