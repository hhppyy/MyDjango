from django.db import models

# Create your models here.

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
    uid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)

class PersonInfo(models.Model):
    uid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    age  = models.IntegerField(null=True)