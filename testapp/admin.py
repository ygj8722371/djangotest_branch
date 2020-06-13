from django.contrib import admin
from testapp.models.project import Project
from testapp.models.module import Module
# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
    list_display = ["name","describe","status","create_time","update_time"]
    search_fields = ["name"]
    list_filter = ["status"]


class ModuleAdmin(admin.ModelAdmin):
    list_display = ["name","describe","create_time","project"]


admin.site.register(Project,ProjectAdmin)
admin.site.register(Module,ModuleAdmin)