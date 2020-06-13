from django.shortcuts import render
from django.shortcuts import HttpResponse,HttpResponseRedirect
from templates import *
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from module_app.models import Module
from module_app.forms import ModuleForm
# Create your views here.


@login_required
def module(request):
    modules = Module.objects.all()
    return render(request,'module.html',{'modules':modules,'type': 'list'})

def add_module(request):
    form = ModuleForm()
    if request.method == 'GET':
        return render(request,'module.html', {'type': 'add','form':form})
    elif request.method == 'POST':
        form = ModuleForm(request.POST)
        if form.is_valid():
            project = form.cleaned_data['project']
            name = form.cleaned_data['name']
            describe = form.cleaned_data['describe']
            if project == '':
                name_error = '项目名不能为空'
                return render(request, 'module.html', {'type': 'add','name_error':name_error})
            else:
                Module.objects.create(project=project,name=name,describe=describe)
                return HttpResponseRedirect('/module/')

def delete_module(request,mid):
    if request.method == 'GET':
        project = Module.objects.get(id=mid)
        project.delete()
        return HttpResponseRedirect('/module/')
    else:
        return HttpResponseRedirect('/module/')

def edit_module(request,mid):
    if request.method == 'GET':
        module = Module.objects.get(id=mid)
        form = ModuleForm(instance=module)
        return render(request, 'module.html', {'type': 'edit','form':form,'id':mid})

    elif request.method == 'POST':
        form = ModuleForm(request.POST)
        if form.is_valid():
            project = form.cleaned_data['project']
            name = form.cleaned_data['name']
            describe = form.cleaned_data['describe']
            m = Module.objects.get(id=mid)
            m.project = project
            m.name = name
            m.describe = describe
            m.save()
            return HttpResponseRedirect('/module/')
