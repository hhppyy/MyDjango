from django.db import models

# Create your models here.
import django.utils.timezone as timezone
class TestTimer(models.Model):
    creattime = models.DateTimeField(default=timezone.now)
    # 创建时间
    updatetime = models.DateTimeField(auto_now=True)
    # 更新时间
    date = models.DateField(default=timezone.now)
    time = models.TimeField(default=timezone.now)


class TestHan(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    pwd = models.IntegerField()
    #bigint
    tel = models.BigIntegerField()
    #text文本
    text = models.TextField()
    # 图片
    img = models.ImageField()
    #日期时间
    timeser = models.DateTimeField()
    #文件
    file = models.FileField()
    #布尔
    status = models.BooleanField()



"""
类名代表了数据库表名，且继承了models.Model，
类里面的字段代表数据表中的字段(name)，
数据类型则由
CharField（相当于varchar）、
IntegerField（相当于int），
max_length 参数限定长度。
"""


# 新建一个PersonInfo类，继承models.Model
class PersonUser(models.Model):
    # 字段名 uid，类型int，主键
    uid = models.IntegerField(primary_key=True)
    # name char 长度30
    name = models.CharField(max_length=30)

class PersonInfo(models.Model):
    uid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    #null=True 可以为空
    age  = models.IntegerField(null=True)
    #blank=True 表示代码中创建数据库记录时该字段可传空白(空串,空字符串).
    add = models.CharField(max_length=30,blank=True)
    email = models.CharField(max_length=30,default='123@qq.com')