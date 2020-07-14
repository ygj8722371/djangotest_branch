"""djangotest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
# import project_app
# import module_app
from user_app import views

#  重构前的数据
# urlpatterns = [
#     # 登录
#     path('admin/', admin.site.urls),
#     path('index/',login_views.index),
#     path('logout/',login_views.logout),
#     path('',login_views.index),
#     # 项目
#     path('project/', project_views.project),
#     path('project/add_project', project_views.add_project),
#     path('project/edit_project/<int:pid>/', project_views.edit_project),
#     path('project/delete_project/<int:pid>/', project_views.delete_project),
#     # 模块
#     path('module/', module_views.module),
#     path('module/add_module', module_views.add_module),
#     path('module/edit_module/<int:mid>/', module_views.edit_module),
#     path('module/delete_module/<int:mid>/', module_views.delete_module),
# ]

urlpatterns = [
    # 登录
    path('admin/', admin.site.urls),
    path('index/',views.index),
    path('loginout/',views.loginout),
    path('',views.index),
    # 项目
    path('project/', include('project_app.urls')),
    # 模块
    path('module/', include('module_app.urls')),
]


