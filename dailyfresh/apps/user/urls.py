from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from apps.user import views
from apps.user.views import RegisterView, ActiveView, LoginView, UserInfoView, UserOrderView, AddressView

urlpatterns = [
    # url(r'^register$', views.register, name='register'), # 注册
    # # url(r'^register_handle$', views.register_handle, name='register_handle'), # 注册处理
    url(r'^register$', RegisterView.as_view(), name='register'),  # 注册  调用类视图的as_view()方法
    url(r'^active/(?P<token>.*)$', ActiveView.as_view(), name='active'),  # 激活用户
    url(r'^login$', LoginView.as_view(), name='login'),  # 登录页面

    # url(r'^$', login_required(UserInfoView.as_view()), name='user'),  #  在这里,调用了login_requird函数装饰视图函数.用户中心-信息
    # url(r'^order$', login_required(UserOrderView.as_view()), name='order'), # 用户中心-订单页
    # url(r'^address$', login_required(AddressView.as_view()), name='address'), # 用户中心-地址页

    url(r'^$', UserInfoView.as_view(), name='user'),  #  在这里,调用了login_requird函数装饰视图函数.用户中心-信息
    url(r'^order$', UserOrderView.as_view(), name='order'), # 用户中心-订单页
    url(r'^address$', AddressView.as_view(), name='address'), # 用户中心-地址页

]
