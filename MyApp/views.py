from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.http import JsonResponse


def archive(request, month, year):
    res = {
        "code": 0,
        "msg": "成功success!",
        "datas": [{
            "month": month,
            "year": year
        }]
    }

    return JsonResponse(res,json_dumps_params={'ensure_ascii':False})

def login_demo(request):
    return render(request, "login.html")



def hello(request):

    res = {
        "code": 0,
        "msg": "成功success!",
        "data": []
    }
    return JsonResponse(res,json_dumps_params={'ensure_ascii':False})


# def hello(request):
#     return HttpResponse("hello,world!")

