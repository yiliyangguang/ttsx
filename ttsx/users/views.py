#coding=utf-8
from django.shortcuts import render,redirect
from hashlib import sha1
from models import UserInfo
from django.http import JsonResponse
from models import *
# Create your views here.
def index(request):
    return render(request,'users/index.html')

def register(request):
    return render(request, 'users/register.html', {'title':'注册'})

def register_handle(request):
    dict = request.POST
    uname = dict.get('user_name')
    list = UserInfo.objects.all()
    for temp in list:
        if uname in temp.uname:
            return JsonResponse({'msg':'hello word'})
    upwd = dict.get('pwd')
    uemail = dict.get('email')

    s1 = sha1()
    s1.update(upwd)
    upwd_sha1 = s1.hexdigest()

    user = UserInfo()
    user.uname = uname
    user.upwd = upwd_sha1
    user.uemail = uemail
    user.save()
    return redirect('/users/login/')
def login(request):
    return render(request, 'users/login.html', {'title':'登陆'})



