import random

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from App.models import Person


def add_persons(request):
    '''批量创建人'''
    for i in range(15):
        person = Person()
        flag = random.randrange(100)
        person.p_name = "Tom%d"% i
        person.p_age = flag
        person.p_sex = flag % 2
        person.save()
    return HttpResponse("批量创建成功!")