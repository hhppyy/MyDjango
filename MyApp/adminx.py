import xadmin
from . import models

"""
在admin.py文件的同一目录新建一个adminx.py(注意只能是adminx.py,不能叫其它的名称)
在adminx.py里与之前的admin.py代码有一些不一样

之前import admin, 这里import xadmin
之前注册表时继承admin.ModelAdmin， 这里继承object
之前inlines 关联的表（class MoreInfo）继承admin.StackedInline， 这里继承object
之前可以有2种注册方式，可以用装饰器方法@admin.register（表类名），这里只能通过xadmin.site.register(表类名, xxx)方式
"""

class ControlStudent(object):
    #显示字段
    list_display = ('student_id','name','age','score')
    #搜索条件
    search_fields = ('name',)
    #每页显示10条
    list_per_page = 10

#注册Student表
xadmin.site.register(models.Student,ControlStudent)



