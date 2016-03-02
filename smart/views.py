#coding:utf-8
import json
from django.http import HttpResponse ,JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from smart.models import *



# Create your views here.

def login(request):
    return render(request, 'login_soft.html')


def index(request):
    print("index!")
    return render(request, 'layout_horizontal_sidebar_menu.html')


def coordinative_project_manage(request):
    print("协作办公-项目管理！")
    #user = User_info(Account='SY1306111',Role=1,Pwd='SY1306111',Name='张帅')
    #user.save()
    return render(request, 'coordinative_project_manage.html')


def system_user_manage_show(request):
    print("系统管理-用户管理")
    users = User_info.objects.filter(isDelete=False)
    return render(request, 'system_user_manage.html', {'users': users})


@csrf_exempt
def system_user_manage_delete(request):
    result = {}
    users = None
    if request.POST.has_key('Account'):
        Account = request.POST['Account']
        users = User_info.objects.filter(Account = Account)
    if users:
        u = User_info.objects.get(Account = Account)
        u.isDelete = True
        u.save()
        result = "1"
        result = json.dumps(result)
    else:
        result = "0"
        result = json.dumps(result)
    return  HttpResponse(result, content_type="application/json")


def system_user_manage_add(request):
    print("添加用户")
    users = User_info.objects.filter(isDelete=False)
    return render(request, 'system_user_manage_add.html', {'users': users})




