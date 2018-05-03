from django.conf.urls import url

from . import views

urlpatterns = [
    # mine
    url(r'^mine/$', views.mine),
    # 注册
    url(r'regist/$', views.regist),
]
