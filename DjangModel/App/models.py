from django.db import models

# Create your models here.

class Person(models.Model):
    p_name = models.CharField(max_length=16, unique=True)
    p_age = models.IntegerField(default=18, db_column='age') # 改P_name 为name
    # False 代表男,True 代表女
    p_sex = models.BooleanField(default=False, db_column='sex')
    # 改类名(字段名)为People
    class Mata:
        db_table = "People"