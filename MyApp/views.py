from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.http import JsonResponse
from .base.common import validateEmail
from .models import Stendent


def post_del(request):
    """删除操作"""
    context = {
        "msg": ""
    }
    if request.method == "GET":
        return render(request,'post_commit.html',context=context)
    elif request.method == "POST":
        qq = request.POST.get('qq', '')
        info = Stendent.objects.filter(qq)
        if not info:
            context['msg'] = 'qq号不存在，请重新输入'
            return render(request,'post_commit.html',context=context)
        else:
            info.delete()
            context['msg'] = '删除成功'
            return render(request,'post_commit.html',context=context)

    else:
        return render(request,'post_commit.html',context=context)




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


def login_demo(request):
    # render 渲染html
    return render(request, "login.html")


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
