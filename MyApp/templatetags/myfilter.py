from django import template

register = template.Library()  # register的名字是固定的,不可改变

#替换字符串的自定义过滤器
@register.filter("replace")
def myreplace(value, arg):
    return value.replace(arg, "!")