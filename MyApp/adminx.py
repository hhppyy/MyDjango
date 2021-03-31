import xadmin
from . import models

class ControlStudent(object):
    #显示字段
    list_display = ('student_id','name','age','score')
    #搜索条件
    search_fields = ('name',)
    #每页显示10条
    list_per_page = 10

#注册Student表
xadmin.site.register(models.Student,ControlStudent)



