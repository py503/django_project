from django.shortcuts import render
from django.template import loader, RequestContext
from django.http import HttpResponse
# Create your views here.


# 自定义返回模板
def my_render(request, template_path, context={}):
    '''主页'''
    # 1.加载模板文件,获取一个模板对象
    temp = loader.get_template(template_path)
    # 2.定义模板上下文,给模板文件传数据
    context = RequestContext(request, context)
    # 3. 模板渲染,产生一个替换后的html内容
    res_html = temp.render(context)
    # 4. 返回应答
    return HttpResponse(res_html)



# /index
def index(request):
    '''主页'''
    # return my_render(request, 'booktest/index.html') # 自定义返回模板,调用my_render函数
    return render(request, 'booktest/index.html') # 调用django自带的.


def child(request):
    '''继承父模板'''
    return render(request, 'booktest/child.html')
