from django.contrib import admin
from django.urls import path
from project_app import views

urlpatterns = [
    # 模块
    path('', views.project),
    path('add_project/', views.add_project),
    path('edit_project/<int:pid>/', views.edit_project),
    path('delete_project/<int:pid>/', views.delete_project),
]