import random

from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render
from Three.models import Student, Stu, Grade

# Create your views here.
from django.template import loader


# def index(request):
#     three_index = loader.get_template("three_index.html")
#     context = {
#         "student_name" : "Sunck"
#         }
#     result = three_index.render(context=context)
#     print(result)
#     return HttpResponse(result)


def index(request):
    context = {
        "student_name": "Sunck"
    }
    return render(request, "three_index.html", context)


def add_student(request):
    student = Student()
    student.s_name = 'Jerry{}'.format(random.randrange(100))
    student.save()
    return HttpResponse("添加成功{}".format(student.s_name))


def get_student(request):
    students = Student.objects.all()
    for student in students:
        print(student.s_name)
    context = {
        "students": students
    }
    # return HttpResponse("Student List{}".format(student.s_name))
    return render(request, "three_getstudent.html", context)


def update_student(request):
    # 查出数据,主键为2 的学生
    student = Student.objects.get(pk=2)
    # 给主键为2的学生改名字
    student.s_name = 'Lee'
    student.save()
    return HttpResponse("改名成功")


def delete_student(request):
    student = Student.objects.get(pk=4)
    student.delete()
    return HttpResponse("Student Delete Success")


def add_stu(request):
    for i in range(1,100):
        student = Stu()
        student.s_name = 'Tom{}{}'.format(i,random.randrange(100))
        student.s_age = 6
        student.s_grade_id = random.randint(1, 6)
        student.save()
    return HttpResponse("添加成功{}".format(student.s_name))


def get_stu(request):
    # 通过stu表查出学生信息
    student = Stu.objects.all()
    context = {
        'student': student
    }
    return render(request, "three_getstulist.html", context)

    # 给出一个学生的名字,查了该学生的班级
    # student = Stu.objects.get(pk=3)
    # stu_name = student.s_name
    # stu_grade = student.s_grade # 班级对象
    # return HttpResponse("name : {},grade : {}".format(stu_name, stu_grade.g_name))


def get_grade(request):
    # 通过班级表grade查出学生信息
    # grade = Grade.objects.get(pk=1)
    grade = Grade.objects.get(g_name ="六班") # 通过g_name设定参数
    students = grade.stu_set.all()  # stu_set 外键中的方法
    context = {
        "grade" : grade,
        "students": students
    }
    return render(request, "three_getgrade.html", context)


def studentpage(request, pageid):
    # 所有学生列表
    allList = Stu.objects.all()
    # 一页显示6条数据
    paginator = Paginator(allList, 6)
    print(type(pageid))
    if pageid == "":
        pageid = 1
    else:
        pageid = int(pageid)
    # 显示第几页数据
    page = paginator.page(pageid)

    return render(request, 'studentpage.html',{"students":page})


def upfile(request):
    """显示上传"""
    return render(request, 'upfile.html')

from django.conf import settings
import os
def savefile(request):
    """判断是否是post请求"""
    if request.method == "POST":
        # 获取POST请求发来的内容
        f = request.FILES['file']
        # 文件在服务器端的路径
        # f.name 为上传过来的文件名
        filepath = os.path.join(settings.MDEIA_ROOT,f.name)
        print(settings.BASE_DIR)
        print(filepath)
        with open(filepath, 'wb') as fp:
            # 分段接收,写入文件. f 是以流形式的
            for info in f.chunks():
                fp.write(info)
        return HttpResponse("上传成功")

    else:
        return HttpResponse("上传失败")
