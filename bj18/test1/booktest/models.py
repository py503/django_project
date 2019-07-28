from django.db import models

# Create your models here.
from tinymce.models import HTMLField


class GoodsTest(models.Model):
    '''测试模型类'''
    STATUS_CHOICES = (
        (0, '下架'),
        (1, '上架'),

    )
    status = models.SmallIntegerField(default=1, choices= STATUS_CHOICES, verbose_name='商品信息')
    # 使用富文本编辑器,要先安装: pip3 install django-tinymce==2.6.0
    detail = HTMLField(verbose_name='商品详情')


    class Meta:
        # 指定表名
        db_table = 'df_goods_test'