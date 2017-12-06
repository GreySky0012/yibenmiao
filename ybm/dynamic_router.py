# coding:utf-8

from __future__ import print_function
from django.shortcuts import render_to_response, HttpResponse, redirect
import ybm


def process(request, **kwargs):
    """接收所有匹配url的请求，根据请求url中的参数，通过反射动态指定view中的方法"""

    app = kwargs.get('app', None)
    function = kwargs.get('function', None)

    try:
        app_name = "ybm.%s.views" % app
        print(app_name)
        moduleObj = __import__(app_name,fromlist=True)
        funcObj = getattr(moduleObj, function)

        # 执行view.py中的函数，并获取其返回值
        result = funcObj(request, kwargs)
    except ImportError:
        # 导入模块失败
        return HttpResponse('导入模块'+app.encode('utf-8')+'失败')
    except AttributeError:
        #加载函数失败
        return HttpResponse('加载函数'+function.encode('utf-8')+'失败')
    except Exception as e:
        # 代码执行异常时，自动跳转到指定页面
        return redirect('/index/index')

    return result
