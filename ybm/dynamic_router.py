# coding:utf-8

from __future__ import print_function
import json
from django.shortcuts import HttpResponse

from ybm.settings import logger


def page(request, **kwargs):
    '''
    接收所有
    :param request:
    :param kwargs:
    :return:
    '''
    return HttpResponse('HTTP Page')


def wrong_api(request, message= ''):
    '''
    api接口出错
    :param request:
    :param message:错误信息
    :return:错误提示
    '''
    if message == '':
        message = '接口错误'
    logger.warning(message)
    return HttpResponse(json.dumps({'code': -1, 'message': message}))


def process(request, **kwargs):
    """接收所有匹配url的请求，根据请求url中的参数，通过反射动态指定view中的方法"""

    app_name = kwargs.get('app', None)
    function_name = kwargs.get('function', None)

    try:
        module_obj = __import__("ybm.%s.views" % app_name, fromlist=True)
        func_obj = getattr(module_obj, function_name)

        # 执行view.py中的函数，并获取其返回值
        result = func_obj(request, kwargs)
    except ImportError:
        # 导入模块失败
        return wrong_api('导入模块' + app_name.encode('utf-8') + '失败')
    except AttributeError:
        # 加载函数失败
        return wrong_api('加载函数' + function_name.encode('utf-8') + '失败')
    except Exception as e:
        # 代码执行异常时，自动跳转到指定页面
        return wrong_api(e.message)

    return result
