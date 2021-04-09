from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.http import HttpResponseRedirect
from .base.common import validateEmail
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password
from .models import Stendent
from django.contrib.auth.models import User
import json
# from django.core import serializers
from django.forms.models import model_to_dict

from rest_framework import viewsets
from rest_framework import serializers
from .models import *
from django.http import QueryDict
from rest_framework.request import Request

# Create your views here.

def get_parameter_dic(requst,*args,**kwargs):
    if isinstance(requst,Request) == False:
        return {}

    query_params = requst.query_params
    if isinstance(query_params,QueryDict):
        query_params = query_params.dict()
    result_data = requst.data
    if isinstance(result_data,QueryDict):
        result_data = result_data.dict()

    if query_params != {}:
        return query_params
    else:
        return result_data

class CardSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RestCard
        fields = "__all__"

class CardViewSet(viewsets.ModelViewSet):
    queryset = RestCard.objects.all()
    serializer_class = CardSerializer

    def get(self,request,*args,**kwargs):
        params = get_parameter_dic(request)
        return JsonResponse(data=params)

    def post(self,request,*args,**kwargs):
        params = get_parameter_dic(request)
        return JsonResponse(data=params)

    def put(self,requset,*args,**kwargs):
        params = get_parameter_dic(requset)
        return JsonResponse(data=params)


def stendent_api4(request):
    if request.method == "GET":
        infos = []
        # values()不带参数默认输出全部字段
        all = Stendent.objects.all().values()
        # 如果值输出name、qq
        # all = Stendent.objects.all().values('name','qq')
        res = {
            "code": 0,
            "msg": "success!",
            "data": {
                "info": list(all),  # 序列化输出
                "total": len(infos)
            }
        }

        return JsonResponse(res, json_dumps_params={'ensure_ascii': False})


def stendent_api3(request):
    if request.method == "GET":
        infos = []
        all = Stendent.objects.all()
        for i in all:
            j = 0
            # model_to_dict 会跳过DateTimeFiled，手动添加
            infos.append(model_to_dict(i))
            # 手动添加时间
            infos[j]['createtime'] = i.creattime
            infos[j]['updatetime'] = i.updatetime
            j += 1
        res = {
            "code": 0,
            "msg": "success!",
            "data": {
                "info": infos,
                "total": len(infos)
            }
        }

        return JsonResponse(res, json_dumps_params={'ensure_ascii': False})


def stendent_api2(request):
    if request.method == "GET":
        datas = {}
        all = Stendent.objects.all()
        datas['infos'] = json.loads(serializers.serialize('json', all))
        datas['total'] = len(all)
        res = {
            "code": 0,
            "msg": "success!",
            "data": datas
        }
        return JsonResponse(res, json_dumps_params={'ensure_ascii': False})


def stendent_api1(request):
    """查询用户信息"""
    if request.method == "GET":
        infos = []
        all = Stendent.objects.all()
        for i in all:
            info = {
                "name": i.name,
                "age": i.age,
                "qq": i.qq,
                "sex": i.sex,
                "add": i.add,
                "email": i.email,
                "createtime": i.creattime,
                "updatetime": i.updatetime,
            }
            infos.append(info)
        res = {
            "code": 0,
            "msg": "sussess!",
            "data": {"infos": infos,  # 序列化输出
                     "totals": len(infos)
                     }
        }
        return JsonResponse(res, json_dumps_params={'ensure_ascii': False})


@login_required
def update_pwd(request):
    """修改密码"""
    res = ""
    if request.method == "GET":
        return render(request, 'update_pwd.html', {'msg': res})
    elif request.method == "POST":
        pwd = request.POST.get('password', '')
        new_pwd = request.POST.get('new', '')

        # 获取登录的用户名
        username = request.user.username
        print('当前登录的用户名为：%s' % username)

        # 校验密码对不对
        user = authenticate(username=username, password=pwd)
        if not user:
            return render(request, 'update_pwd.html', {'msg': '原密码输入错误，请重新输入'})
        elif new_pwd == pwd:
            return render(request, 'update_pwd.html', {'msg': '新密码与旧密码一致，请重新输入'})
        else:
            # 修改密码
            user.set_password(new_pwd)
            user.save()
            # return render(request,'update_pwd.html',{'msg': '修改密码成功'})
            # 修改成功后跳转至登录页面
            return HttpResponseRedirect('/login/')


def logoutView(request):
    """退出登录"""
    logout(request)  # 这个方法会将存储在用户session数据全部清空
    return render(request, 'login.html', {'msg': ""})


def register(request):
    """注册"""
    if request.method == "POST":
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        email = request.POST.get('email', '')
        # 查询是否有此用户
        user_info = User.objects.filter(username=username)
        email_info = User.objects.filter(email=email)
        email_l = validateEmail(email)
        if user_info:
            # 如果存在，说明已经注册过，给出提示
            return render(request, 'register.html', {'msg': '%s账号已经注册过了' % username})
        else:
            if email_info:
                # 检查邮箱是否存在
                return render(request, 'register.html', {'msg': '%s邮箱已经存在，请更换' % email})
            # 判断前端输入的邮箱格式是否正确
            elif not email_l:
                return render(request, 'register.html', {'msg': '请输入正确的邮箱格式'})
            else:
                # 注册
                user1 = User.objects.create_user(username=username,
                                                 password=password,
                                                 email=email)
                user1.save()
                return render(request, 'register.html', {'msg': '注册成功'})
    else:
        return render(request, 'register.html', {'msg': ''})


def login_demo(request):
    """登录"""
    if request.method == "POST":
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        # 登录认证
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:  # 判断用户是否有效 Ture 为有效，False为无效
                # 调用登录方法，添加session
                # login(request, user=user)
                # request.session['user'] = username
                # # 302重定向至
                # return HttpResponseRedirect('/update_pwd/')
                # return render(request, 'login.html', {'msg': '登录成功'})

                # 添加cookie
                response = redirect("/update_pwd/")
                # response.set_cookie('user',username)
                response.set_signed_cookie('user', username, salt="salt")

                return response

            else:
                return render(request, 'login.html', {'msg': '账号被锁定'})
        else:
            return render(request, 'login.html', {'msg': '账号密码错误'})
    else:
        return render(request, "login.html", {'msg': ''})


# 添加访问权限设置
# @login_required
def select_all(request):
    """查询User全表信息，获取user、pwd、email信息"""
    users = ""
    pwds = ""
    mails = ""
    # 查询全表信息
    res = User.objects.all()  # 迭代对象queryset

    for i in res:
        users += " " + i.username
        pwds += " " + i.password
        mails += " " + i.email

    return HttpResponse("""<p>查询user结果：%s</p>
                        <p>查询password结果：%s</p>
                        <p>查询email结果：%s</p>""" % (users, pwds, mails))


def post_del(request):
    """删除操作"""
    context = {
        "msg": ""
    }
    if request.method == "GET":
        return render(request, 'post_commit.html', context=context)
    elif request.method == "POST":
        qq = request.POST.get('qq', '')
        info = Stendent.objects.filter(qq=qq)
        if not info:
            context['msg'] = 'qq号不存在，请重新输入'
            return render(request, 'post_commit.html', context=context)
        else:
            # 删除
            # 删除name=yoyo1的数据
            # info = PersonInfo.objects.get(name='yoyo1')
            # info.delete()
            # 另外一种方式,删除全部查询的结果
            # PersonInfo.objects.filter(name='yoyo1').delete()
            # 删除所有数据
            # PersonInfo.objects.all().delete()

            info.delete()
            context['msg'] = '删除成功'
            return render(request, 'post_commit.html', context=context)

    else:
        return render(request, 'post_commit.html', context=context)


def post_update(request):
    # Form表单修改数据
    context = {
        "msg": ""
    }

    if request.method == "GET":
        return render(request, 'post_commit.html', context=context)

    elif request.method == "POST":
        name = request.POST.get('name', '')
        age = request.POST.get('age', '')
        qq = request.POST.get('qq', '')
        sex = request.POST.get('sex', '')
        add = request.POST.get('add', '')
        email = request.POST.get('email', '')

        # 以qq作为唯一条件进行查询
        info = Stendent.objects.filter(qq=qq)
        new_name = Stendent.objects.filter(name=name)
        new_email = Stendent.objects.filter(email=email)

        if not info:
            context['msg'] = 'qq号不存在，请更换'
            return render(request, 'post_commit.html', context=context)
        elif new_name:
            if new_name[0].name == name:
                info[0].name = name
                info[0].age = age
                info[0].sex = sex
                info[0].add = add
                info[0].email = email
                info[0].save()
                context['msg'] = "修改成功"
            else:
                context['msg'] = "用户名已经存在，请更换"
            return render(request, 'post_commit.html', context=context)
        # 判断邮箱是否已经存在
        elif new_email:
            if new_email[0].email == email:
                info[0].name = name
                info[0].age = age
                info[0].sex = sex
                info[0].add = add
                info[0].email = email
                info[0].save()
                context['msg'] = "修改成功"
            else:
                context['msg'] = "邮箱已经存在，请更换"
            return render(request, 'post_commit.html', context=context)
        # 判断前端输入的邮箱格式是否正确
        elif not validateEmail(email):
            context['msg'] = "请输入正确的邮箱格式"
            return render(request, 'post_commit.html', context=context)
        else:
            # filter查询出是list，取第一个
            info[0].name = name
            info[0].age = age
            info[0].sex = sex
            info[0].add = add
            info[0].email = email
            info[0].save()

            context['msg'] = '修改成功'
            return render(request, 'post_commit.html', context=context)
    else:
        return render(request, 'post_commit.html', context=context)


def post_insert(request):
    # Form表单添加数据
    context = {
        "msg": ""
    }
    if request.method == "GET":
        # 判断如果是get请求，返回页面
        return render(request, "post_commit.html", context=context)
    elif request.method == "POST":
        # 判断post请求
        # request.POST.get获取前端页面输入值，如果没有获取到默认为空
        name = request.POST.get('name', '')
        age = request.POST.get('age', '')
        sex = request.POST.get('sex', '')
        qq = request.POST.get('qq', '')
        add = request.POST.get('add', '')
        email = request.POST.get('email', '')
        print(qq)
        new_qq = Stendent.objects.filter(qq=qq)
        print(len(new_qq))
        new_name = Stendent.objects.filter(name=name)
        print(len(new_name))
        new_email = Stendent.objects.filter(email=email)
        print(len(new_email))
        email_l = validateEmail(email)
        # 判断用户名是否已经存在
        if new_name:
            context['msg'] = "用户名已经存在，请更换"
            return render(request, 'post_commit.html', context=context)
        # 判断qq是否已经存在
        elif new_qq:
            context['msg'] = "qq已经存在，请更换"
            return render(request, 'post_commit.html', context=context)
        # 判断邮箱是否已经存在
        elif new_email:
            context['msg'] = "邮箱已经存在，请更换"
            return render(request, 'post_commit.html', context=context)
        # 判断前端输入的邮箱格式是否正确
        elif not email_l:
            context['msg'] = "请输入正确的邮箱格式"
            return render(request, 'post_commit.html', context=context)

        else:
            # 不存在就添加
            # 第一种
            # info = Stendent()
            # info.name = name
            # info.age = age
            # info.qq = qq
            # info.add = add
            # info.email = email
            # info.sex = sex
            # 第二种
            info = Stendent(name=name,
                            age=age,
                            add=add,
                            qq=qq,
                            sex=sex,
                            email=email)
            info.save()
            context['msg'] = '提交成功'
            return render(request, 'post_commit.html', context=context)
    else:
        return render(request, 'post_commit.html', context=context)


def get_sel(request):
    """get查询"""
    if request.method == "GET":
        qq_num = request.GET.get('qq', '')  # 如果没获取到，默认空字符
        print(qq_num)
    try:
        info = Stendent.objects.get(qq=qq_num)  # 查询的结果是对象
    except:
        print('未查到结果，qq=%s' % qq_num)
        info = None
    print('不能查询出，查询结果：%s' % info)
    context = {"info": info}
    return render(request, 'get_sel.html', context=context)


def my_filter(request):
    context = {
        "name": "莫使娇躯空对月",
        "n_name": "宇宇+",
        "age": 18,
        "fancy": ["python", "django", "pytest"],
        "blog": {
            "url": "https://home.cnblogs.com/u/xiaoyujuan",
            "img": "https://pic.cnblogs.com/avatar/1001971/20190703151818.png"
        }
    }
    return render(request, 'my_filter.html', context=context)


def default_value(request):
    context = {
        "name": "莫使娇躯空对月",
        "n_name": "",
        "age": 18,
        "fancy": ["python", "django", "pytest"],
        "blog": {
            "url": "https://home.cnblogs.com/u/xiaoyujuan",
            "img": "https://pic.cnblogs.com/avatar/1001971/20190703151818.png"
        }
    }
    return render(request, 'default_value.html', context=context)


def include_common(request):
    context = {
        "title": "导入公共模板"
    }
    return render(request, 'include_common.html', context=context)


def write_father(request):
    context = {
        "title": "重写父级模板"
    }
    return render(request, "write_father.html", context=context)


def extend_l(request):
    return render(request, "extends_base.html")


def iflist(request):
    name_list = [
        {
            "type": "科普读物",
            "value": ["宇宙知识", "百科知识", "科学世界", "生物世界"]
        },
        {
            "type": "计算结/网络",
            "value": ["Java", "Python", "Php"]
        },
        {
            "type": "建筑",
            "value": ["标准/规范", "室内设计", "建筑科学", "建筑文化"]
        }
    ]
    context = {"name_list": name_list}
    return render(request, "if_params.html", context=context)


def looplist(request):
    name_list = [
        {
            "type": "科普读物",
            "value": ["宇宙知识", "百科知识", "科学世界", "生物世界"]
        },
        {
            "type": "计算结/网络",
            "value": ["Java", "Python", "Php"]
        },
        {
            "type": "建筑",
            "value": ["标准/规范", "室内设计", "建筑科学", "建筑文化"]
        }
    ]
    context = {"name_list": name_list}
    return render(request, "forloop_params.html", context=context)


def no_navlist(request):
    context = {"name_list1": []}
    return render(request, "for_params.html", context=context)


def navlist(request):
    name_list = [
        {
            "type": "科普读物",
            "value": ["宇宙知识", "百科知识", "科学世界", "生物世界"]
        },
        {
            "type": "计算结/网络",
            "value": ["Java", "Python", "Php"]
        },
        {
            "type": "建筑",
            "value": ["标准/规范", "室内设计", "建筑科学", "建筑文化"]
        }
    ]
    context = {"name_list": name_list}
    return render(request, "for_params.html", context=context)


def personalView(request):
    """
    render(request, template_name, context=None, content_type=None, status=None, using=None)
    request： 是一个固定参数, 没什么好讲的。
    template_name：templates 中定义的文件, 要注意路径名. 比如'templates\polls\index.html', 参数就要写‘polls\index.html'
    context：要传入文件中用于渲染呈现的数据, 默认是字典格式
    content_type：生成的文档要使用的mime 类型。默认为default_content_type 设置的值。
    status： http的响应代码,默认是200.
    using：用于加载模板使用的模板引擎的名称
    :param request:
    :return:
    """
    context = {
        "name": "莫使娇躯空对月",
        "n_name": "xiaoyu",
        "age": 18,
        "fancy": ["python", "django", "pytest"],
        "blog": {
            "url": "https://home.cnblogs.com/u/xiaoyujuan",
            "img": "https://pic.cnblogs.com/avatar/1001971/20190703151818.png"
        }
    }

    # 类对象取值
    class Myblog():
        def __init__(self):
            self.name = "娇躯"
            self.age = 20

        def guanzhu(self):
            return 100

        def fensi(self):
            return 1000

    myblog = Myblog()
    context["myblog"] = myblog  # 类的实例化添加进入context

    return render(request, "personal.html", context=context)


def lianjie(request):
    # render 渲染html
    return render(request, "MB_params.html", {'year': "2020"})


def archive(request, month, year):
    # 设置 动态参数year month
    res = {
        "code": 0,
        "msg": "成功success!",
        "datas": [{
            "month": month,
            "year": year
        }]
    }
    # 返回json对象
    # json_dumps_params={'ensure_ascii':False} 防止中文乱码
    return JsonResponse(res, json_dumps_params={'ensure_ascii': False})


def hello(request):
    res = {
        "code": 0,
        "msg": "成功success!",
        "data": []
    }
    # 返回json对象
    # json_dumps_params={'ensure_ascii':False} 防止中文乱码
    return JsonResponse(res, json_dumps_params={'ensure_ascii': False})

# def hello(request):
#     return HttpResponse("hello,world!")
