from django.db import models


# Create your models here.
class Grade(models.Model):
    # 班级信息
    g_name = models.CharField(max_length=32)

    # 重写str方法
    def __str__(self):
        return self.g_name


class Student(models.Model):
    # 学生信息
    s_name = models.CharField(max_length=16)
    s_age = models.IntegerField(default=1)


class Stu(models.Model):
    # 学生信息
    s_name = models.CharField(verbose_name='姓名', max_length=16) # verbose_name:指定中文名
    s_age = models.IntegerField(default=1)
    # 添加外键
    s_grade = models.ForeignKey(Grade)

    # 重写str方法
    def __str__(self):
        return self.s_name
