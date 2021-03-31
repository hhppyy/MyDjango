from django.db import models
import django.utils.timezone as timezone


#设置datetime、time类型同步到数据库不是datetime(6)
from django.db.backends.mysql.base import DatabaseFeatures # 关键设置
DatabaseFeatures.supports_microsecond_precision = False # 关键设置


# Create your models here.


class Student(models.Model):
    '''学生成绩'''
    student_id = models.CharField(verbose_name='学生id',max_length=30)
    name = models.CharField(verbose_name='姓名',max_length=30)
    age = models.IntegerField(verbose_name='年龄')
    score = models.IntegerField(verbose_name='分数')

    class Meta:
        verbose_name = "学生成绩表"
        verbose_name_plural = verbose_name


class Stendent(models.Model):
    """个人信息表"""
    name = models.CharField(verbose_name='姓名',max_length=30)
    age = models.IntegerField(verbose_name='年龄')
    qq = models.IntegerField(verbose_name='qq号')
    sex = models.CharField(verbose_name='性别',max_length=50)
    add = models.CharField(verbose_name='地址',max_length=30)
    email = models.CharField(verbose_name='邮箱',max_length=50)
    creattime = models.DateTimeField(verbose_name='创建时间',auto_now_add=True)
    # 创建时间
    updatetime = models.DateTimeField(verbose_name='更新时间',auto_now=True)

    def __str__(self):
        """返回一个字符串，当做这个对象的描写，返回一个对象的描述信息
        self.__doc__为类的描述信息 --个人信息表
        self.name为表中的name字段的值
        """

        return self.__doc__ + ":" + self.name

    class Meta:
        """verbose_name_plural属性是写在class Meta下的, class Meta嵌套在class PersonInfo里
        在页面中MyApp中展示信息
        """
        verbose_name_plural = "个人信息表"


class TestTimer(models.Model):
    creattime = models.DateTimeField(auto_now_add=True)
    # 创建时间
    updatetime = models.DateTimeField(auto_now=True)
    # 更新时间
    date = models.DateField(auto_now=True)
    time = models.TimeField(auto_now=True)


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