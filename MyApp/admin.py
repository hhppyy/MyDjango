from django.contrib import admin
from . import models


# Register your models here.
#设置首页、标题、登录页面
admin.site.site_header = 'MyApp项目管理系统'
admin.site.site_title = 'MyApp登录系统后台'
admin.site.index_title = 'MyApp后台管理'



# 注册模型

# 第一种注册方法，装饰器使用（装饰器参数为models中模型）
# @admin.register(models.Stendent)
# class ControlStendent(admin.ModelAdmin):
#     """自定义列表中栏目 添加list_dispaly属性"""
#     list_display = ('id', 'name', 'age', 'qq', 'sex', 'add', 'email', 'creattime', 'updatetime')
#     # 添加搜索,必须是列表或元组
#     search_fields = ('name',)

#第二种注册方法
class ControlStendent(admin.ModelAdmin):
    """自定义列表中栏目 添加list_dispaly属性"""
    list_display = ('id', 'name', 'age', 'qq', 'sex', 'add', 'email', 'creattime', 'updatetime')
    # 添加搜索,必须是列表或元组
    search_fields = ('name',)
    #排序，设置默认排序字段，负号表示降序排序
    ordering = ('-qq',)
    #list_editable 设置默认可编辑字段
    list_editable = ['name',]

admin.site.register(models.Stendent, ControlStendent)  # 注册表
