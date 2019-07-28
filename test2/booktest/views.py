from django.shortcuts import render, redirect
from booktest.models import BookInfo, AreaInfo
from datetime import date
from django.http import HttpResponse, HttpResponseRedirect
from django.http import HttpResponse
from django.db import models

# Create your views here.
def index(request):
    '''显示图书信息'''
    # 1. 查询出所有图书信息
    books = BookInfo.objects.all()
    # 2. 使用模板
    return render(request, 'booktest/index.html', {'books': books})


def create(request):
    '''新增一本图书'''
    # 1. 创建BookInfo对象
    books = BookInfo()
    # books.btitle = "流星蝴蝶剑"
    # books.bpub_date = date(1990, 1, 1)
    # 2. 保存到数据库
    # books.save()
    books.btitle = "仙鹤神针"
    books.save()
    # 3. 返回应答,让浏览器再访问/index,重定向
    # return HttpResponseRedirect('/index')
    return redirect('/index')
    # return HttpResponse("ok") # 没有重定向,直接返回/create  url


def delete(request, bid):
    '''

    :param request:
    :param bid: 图书id
    :return: 重定向后的/index页面
    '''
    # 1. 通过bid获取图书对象
    book = BookInfo.objects.get(id=bid)
    # 2. 删除
    book.delete()
    # 3. 重定向,让浏览器访问/index
    # return HttpResponseRedirect('/index')
    return redirect('/index')


def areas(request):
    '''获取广州市的上级地区和下级地区信息'''
    # 1. 获取广州市的信息
    area = AreaInfo.objects.get(atitle='广州市')
    # 2. 查询广州市的上级信息
    parent = area.aParent
    # 3. 查询广州市的下级信息,一对多
    children = area.areainfo_set.all()
    # 使用模板
    return render(request, 'booktest/areas.html', {'area':area,
                                                   'parent':parent,'children':children})
