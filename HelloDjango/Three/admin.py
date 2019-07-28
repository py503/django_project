from django.contrib import admin

# Register your models here.
from Three.models import Stu, Grade

class StuAdmin(admin.ModelAdmin):
    '''学生模型管理类'''
    list_per_page = 10 # 指定每页显示10条数据
    list_display = ['id','s_name','s_grade']
    actions_on_bottom = True
    # 显示搜索框
    search_fields = ['s_name'] # 这里是以s_name 为搜索内容


admin.site.register(Stu, StuAdmin) # 注册所有的类

