from django import forms
from testapp.models.project import Project
from testapp.models.module import Module

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name','describe','status']

class ModuleForm(forms.ModelForm):
    class Meta:
        model = Module
        fields = ['project','name','describe']