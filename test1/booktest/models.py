from django.db import models
# 设计和表对应的类,模型类
# Create your models here.

# 图书类
class BookInfo(models.Model):
    """图书模型类"""
    # 图书名称,CharField说明是一个字符串,max_length指定字\
    # 符串的最大长度
    btitle = models.CharField(max_length=20)
    # 出版日期,DateField说明是一个日期类型
    bpub_date = models.DateField()