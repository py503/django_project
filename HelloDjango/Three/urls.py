from django.conf.urls import url

from Three import views

urlpatterns = [
    url(r'^index/', views.index),
    url(r'^addstudent/', views.add_student),
    url(r'^getstudent/', views.get_student),
    url(r'^updatestudent/', views.update_student),
    url(r'^deletestudent', views.delete_student),
    url(r'^addstu/', views.add_stu),
    url(r'^getstu/', views.get_stu),
    url(r'^getgrade/', views.get_grade),

    url(r'^upfile/', views.upfile),
    url(r'^savefile/', views.savefile),

    url(r'^studentpage/?(\d*)/$', views.studentpage),
]
