
import traceback

from django.http import HttpResponse


def decorator(func):
    # 装饰器方法：用来给函数添加功能，当函数执行失败的时候打印错误信息再抛出异常
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            #打印出错的位置
            return HttpResponse(traceback.format_exc().replace('\n','<br/>'))
    return wrapper