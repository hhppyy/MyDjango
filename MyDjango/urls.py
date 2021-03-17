"""MyDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django.conf.urls import url
from MyApp import views

"""
path:匹配绝对路径
url:支持正则，django2.x版本推荐
re_path:支持正则，django1.x版本推荐
"""

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^hello$', views.hello),
    # url 设置名称，方便在其他地方引用
    url(r'^login/$', views.login_demo, name="login"),
    # path('yuyu/archive/<year>/<month>.html', views.archive),
    url(r'^yuyu/archive/(?P<year>[0-9]{4})/(?P<month>[0-9]{2}).html$', views.archive),
    url(r'^lianjie$', views.lianjie),
    url(r'^personal$', views.personalView),
    url(r'^navlist$', views.navlist),
    url(r'^no_navlist$', views.no_navlist),
    url(r'^looplist$', views.looplist),
    url(r'^iflist$', views.iflist),
    url(r'^extend_l$', views.extend_l),
]
