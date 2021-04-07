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
#注册文件和图片表

class ContorlFiles(object):
    list_dispaly = ['title','add_time']

xadmin.site.register(models.FileImages,ContorlFiles)

#注册表关联

class MoreInfo(object):
    model = models.CardDetail

class ContorlCard(object):
    #展示字段
    list_display = ["card_id","card_user","手机号","城市","create_time"]
    #关联表CardDetail。在页面显示
    inlines = [MoreInfo]
    #查询关联表的字段，并将关联表字段展示在list_display中
    def 手机号(self,obj):
        return obj.carddetail.tel
    def 城市(self,obj):
        return obj.carddetail.city

#注册Card，关联CardDetail
xadmin.site.register(models.Card,ContorlCard)

class ControlStudent(object):
    #显示字段
    list_display = ('student_id','name','age','score')
    #搜索条件
    search_fields = ('name',)
    #每页显示10条
    list_per_page = 10

#注册Student表
xadmin.site.register(models.Student,ControlStudent)



