from django import template
import time

register = template.Library()  # register的名字是固定的,不可改变

#获取当前时间的自定义标签
@register.simple_tag(name="current_time")
def get_current_time():
    timestr = time.strftime("%Y-%m-%d %H:%M:%S")
    return timestr
