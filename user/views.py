# -*-coding:utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators import csrf
from  user.models import User as user

import json
# Create your views here.


def selectUserAll(request):
    userlist = []
    list = {}
    user_list = user.objects.all()
    if(len(user_list) > 0):
        for value in user_list:
            u = user.getSelectAll(value)
            userlist.append(u)
        list['code'] = '1'
        list['message'] = '查询成功'
        list['data'] = userlist
    else :
        list['code'] = '-1'
        list['message'] = '暂无数据'
    return HttpResponse(json.dumps(list, ensure_ascii=False), content_type="application/json")