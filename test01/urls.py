"""test01 URL Configuration

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
from django.conf.urls import url

from user import views as user

urlpatterns = [
    # 获取所有的用户信息
    url(r'selectUserAll$', user.selectUserAll),
    # 根据用户的ID获取用户的信息
    url(r'getSelectById', user.getSelectById),
    # 添加用户
    url(r'addUser', user.addUser),
]