from django.db import models


# Create your models here.
class BookInfo(models.Model):
    '''图书模型类'''
    # 图书名称
    btitle = models.CharField(max_length=20)
    # btitle = models.CharField(max_length=20, unique=True) # 唯一,btitle不能重复
    # 出版日期
    bpub_date = models.DateField()
    # bpub_date = models.DateField(auto_now_add=True) # 自动创建时间,不用另外添加
    # bpub_date = models.DateField(auto_now_add=True) # 更新时间
    # 阅读量
    bread = models.IntegerField(default=0)
    # 评论量
    bcomment = models.IntegerField(default=0)
    # 删除标记
    isDelete = models.BooleanField(default=False)


class HeroInfo(models.Model):
    """英雄人物模型类"""
    # 英雄名
    hname = models.CharField(max_length=20)
    # 性别
    hgender = models.BooleanField(default=False)
    # 备注
    # 对比: null是数据库范畴的概念，blank是后台管理页面表单验证范畴的
    hcomment = models.CharField(max_length=200,null=True, blank=True) # 内容可以为空
    # 关系属性
    hbook = models.ForeignKey('BookInfo')
    # 删除标记
    isDelete = models.BooleanField(default=False)


class AreaInfo(models.Model):
    '''地区模型类'''
    # 地区名称
    atitle = models.CharField(max_length=20)
    # 关系属性, 代表当前地区的父级地区
    aParent = models.ForeignKey('self', null=True, blank=True)