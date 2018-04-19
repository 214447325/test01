# -*-coding:utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_GET
from  user.models import User as user

import json
# Create your views here.

@csrf_exempt
@require_GET
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
    else:
        list['code'] = '-1'
        list['message'] = '暂无数据'
    return HttpResponse(json.dumps(list, ensure_ascii=False), content_type="application/json")

@csrf_exempt
@require_GET
def getSelectById(request):
    list = {}
    id = request.GET['id']
    if(len(id) > 0):
        if(id.isdigit):
            user_list_info = user.objects.get(id=id)
            user_list = user.getSelectAll(user_list_info)
            list['code'] = '1'
            list['message'] = '查询成功'
            list['data'] = user_list
        else:
            list['code'] = '-1'
            list['message'] = '参数类型错误'
    else:
        list['code'] = '-2'
        list['message'] = '缺少参数'
    return HttpResponse(json.dumps(list, ensure_ascii=False), content_type="application/json")
