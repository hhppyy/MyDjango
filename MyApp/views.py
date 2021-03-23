from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.http import JsonResponse


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
    context= {"name_list": name_list}
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
    context= {"name_list": name_list}
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
    context= {"name_list": name_list}
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
    #类对象取值
    class Myblog():
        def __init__(self):
            self.name = "娇躯"
            self.age = 20

        def guanzhu(self):
            return 100

        def fensi(self):
            return 1000

    myblog = Myblog()
    context["myblog"] = myblog #类的实例化添加进入context

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
