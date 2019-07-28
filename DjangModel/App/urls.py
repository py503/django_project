from django.conf.urls import url

from App import views

urlpatterns = [
    url(r'^addpersons/', views.add_persons),
]