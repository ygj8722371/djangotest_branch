from django.shortcuts import render
from django.shortcuts import HttpResponse,HttpResponseRedirect
from templates import *
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from project_app.models import Project
from project_app.forms import ProjectForm

# Create your views here.

@login_required
def project(request):
    projects = Project.objects.all()
    return render(request,'project.html',{'projects':projects,
                                          'type':'list'})

def add_project(request):
    if request.method == 'GET':
        return render(request,'project.html', {'type': 'add'})
    elif request.method == 'POST':
        name = request.POST.get('name','')
        describe = request.POST.get('describe','')
        status = request.POST.get('status','')
        if name == '':
            name_error = '项目名不能为空'
            return render(request, 'project.html', {'type': 'add','name_error':name_error})
        else:
            Project.objects.create(name=name,describe=describe,status=status)
            return HttpResponseRedirect('/project/')

def delete_project(request,pid):
    if request.method == 'GET':
        project = Project.objects.get(id=pid)
        project.delete()
        return HttpResponseRedirect('/project/')
    else:
        return HttpResponseRedirect('/project/')

def edit_project(request,pid):
    if request.method == 'GET':
        project = Project.objects.get(id=pid)
        form = ProjectForm(instance=project)
        return render(request, 'project.html', {'type': 'edit','form':form,'id':pid})

    elif request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            describe = form.cleaned_data['describe']
            status = form.cleaned_data['status']
            p = Project.objects.get(id=pid)
            p.name = name
            p.describe = describe
            p.status = status
            p.save()
            return HttpResponseRedirect('/project/')


