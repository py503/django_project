from django.conf.urls import url

from apps.goods import views
from apps.goods.views import IndexView, DetailView

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),  # 首页
    url(r'^index$', IndexView.as_view(), name='index'),  # 首页
    # url(r'^index.html$', IndexView.as_view(), name='index'),  # 首页
    url(r'^goods/(?P<goods_id>\d+)$', DetailView.as_view(), name='detail'), # 详情页

]
