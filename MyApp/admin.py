from django.contrib import admin
from . import models
# Register your models here.
#注册模型

class ControlStendent(admin.ModelAdmin):
    """自定义列表中栏目 添加list_dispaly属性"""
    list_display = ('id','name','age','qq','sex','add','email','creattime','updatetime')
    #添加搜索,必须是列表或元组
    search_fields = ('name',)
admin.site.register(models.Stendent,ControlStendent) #注册表