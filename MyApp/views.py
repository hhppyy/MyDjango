from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.http import JsonResponse


def lianjie(request):
    # render 渲染html
    return render(request, "MB_params.html", {'year':"2020"})



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
    return JsonResponse(res,json_dumps_params={'ensure_ascii':False})

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
    return JsonResponse(res,json_dumps_params={'ensure_ascii':False})


# def hello(request):
#     return HttpResponse("hello,world!")

