from django.shortcuts import render
from django.shortcuts import HttpResponse,HttpResponseRedirect
from templates import *
from django.contrib import auth
# Create your views here.


def index(request):
    if request.method == 'GET':
        return render(request,'index.html')
    else:
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        if username == '' or password == '':
            return render(request,'index.html',{'error':'用户名或者密码为空'})
        user = auth.authenticate(username=username,password=password)
        if user is None:
            return render(request, 'index.html', {'error': '用户名或者密码错误'})
        else:
            auth.login(request,user)
            return HttpResponseRedirect('/project')

def loginout(request):
    auth.logout(request)
    return HttpResponseRedirect('/index')