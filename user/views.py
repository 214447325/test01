# -*-coding:utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_GET
from django.core.cache import cache
from  user.models import User
import user
import time
import json
# Create your views here.

'''
1:数据库查询成功
-1:暂无数据
-2:数据类型错误
-3:缺少参数
'''

@csrf_exempt
@require_GET
def selectUserAll(request):
    userlist = []
    list = {}
    try:
        user_list = User.objects.all()
        if len(user_list) > 0:
            for value in user_list:
                u = User.getSelectAll(value)
                userlist.append(u)
            list['code'] = '1'
            list['message'] = '查询成功'
            list['data'] = userlist
        else:
            list['code'] = '-1'
            list['message'] = '暂无数据'
    except:
        list['code'] = '-1'
        list['message'] = '暂无数据'
    return HttpResponse(json.dumps(list, ensure_ascii=False), content_type="application/json")

@csrf_exempt
@require_GET
def getSelectById(request):
    list = {}
    try:
        id = request.GET.get('id')
        if not id is None:
            if (len(id) > 0):
                if (id.isdigit()):
                    user_list_info = User.objects.get(id=id)
                    user_list = User.getSelectAll(user_list_info)
                    list['code'] = '1'
                    list['message'] = '查询成功'
                    list['data'] = user_list
                else:
                    list['code'] = '-2'
                    list['message'] = '用户数据不合法'
            else:
                list['code'] = '-1'
                list['message'] = '暂无数据'
        else:
            list['code'] = '-3'
            list['message'] = '缺少参数'
    except:
        list['code'] = '-3'
        list['message'] = '缺少参数'
    return HttpResponse(json.dumps(list, ensure_ascii=False), content_type="application/json")

@csrf_exempt
@require_GET
def addUser(request):
    list = {}
    try:
        name = request.GET.get('name')
        address = request.GET.get('address')
        # birthday = request.GET['birthday']
        # if birthday.strip() == '':
        #     t = time.strftime('%Y-%m-%d', time.localtime())
        #     # t = time.strptime('2016-05-09', '%Y-%m-%d')
        # else:
        # t = time.strptime(birthday, '%Y-%m-%d')
        # t = time.strftime('%Y-%m-%d',time.localtime())
        # t = time.strptime('2016-05-09', '%Y-%m-%d')

        # 判断用户的姓名是否为空，如果为空则不能添加用户
        if name is None:
            list['code'] = '-1'
            list['message'] = '缺少用户名'
            return HttpResponse(json.dumps(list, ensure_ascii=False), content_type="application/json")
        # 判断用户的地址是否为空如果为空则不能添加用户
        if address is None:
            list['code'] = '-1'
            list['message'] = '缺少用户地址'
            return HttpResponse(json.dumps(list, ensure_ascii=False), content_type="application/json")

        if (not name is None) and (not address is None):
            birthday = request.GET.get('birthday')

            # 判断用户的生日如果该用户的生日没有传递，默认为系统当前的年月日
            if birthday is None:
                birthday = time.strftime('%Y-%m-%d',time.localtime())
            u = User(name=name, address=address, birthday=birthday)
            u.save()
            list['code'] = '1'
            list['message'] = '添加成功'
            return HttpResponse(json.dumps(list, ensure_ascii=False), content_type="application/json")
    except:
        list['code'] = '-1'
        list['message'] = '添加失败'
        return HttpResponse(json.dumps(list, ensure_ascii=False), content_type="application/json")

# 根据用户的ID修改用户的数据
@csrf_exempt
@require_GET
def updateUserInfo(request):
    list = {}
    try:
        id = request.GET.get('id')
        name = request.GET.get('name')
        address = request.GET.get('address')
        birthday = request.GET.get('birthday')
        if id is None:
            list.__setitem__('code', '-3')
            list.__setitem__('message', '该信息不存在')
        else:
            if(name is None) and (address is None) and (birthday is None):
                list.__setitem__('code', '-3')
                list.__setitem__('message', '缺少用户修改的信息')
            else:
                u = User.objects.get(id=id)
                if not name is None:
                    u.name = name
                if not address is None:
                    u.address = address
                if not birthday is None:
                    u.birthday = birthday
                u.save()
                list.__setitem__('code','1')
                list.__setitem__('message','修改成功')
        return HttpResponse(json.dumps(list, ensure_ascii=False), content_type="application/json")
    except:
        list.__setitem__('code','-1')
        list.__setitem__('message','暂无数据')
        return HttpResponse(json.dumps(list, ensure_ascii=False),content_type="application/json")

# 删除用户的信息并且把用户的原始信息保存在redis中
@csrf_exempt
@require_GET
def deleteUserInfo(request):
    list = {}
    try:
        id = request.GET.get('id')
        u = User.objects.get(id=id)
        u_info = User.getSelectAll(u)
        cache.set(id,u_info,timeout=None)
        u.delete()
        list.__setitem__('code', '1')
        list.__setitem__('message', '删除成功')
        return HttpResponse(json.dumps(list, ensure_ascii=False), content_type="application/json")
    except:
        list.__setitem__('code', '-1')
        list.__setitem__('message', '暂无数据')
        return HttpResponse(json.dumps(list, ensure_ascii=False), content_type="application/json")