# -*- coding: utf-8 -*-#

# ------------------------------------------------------------------------------
# Name:         decorator
# Description:  
# Author:       Allen
# Time:         2020/12/25 10:25
# ------------------------------------------------------------------------------
import functools
import inspect


class OpenApiDecorate:
    """API Interface修饰符
        name:API标识符，用于Wiki文件、内部标记等
        group:分组，未做控制，可自由提供分组
        description:API描述，共DOC使用
        permission:BasePermission子类，提供验权
    """

    def __init__(self, category="其他", name=None, permission=None, test=None, prefix=None, track=None):
        self.category = category
        self.name = name
        self.permission = permission
        self.test = test
        self.prefix = prefix
        self.track = track  # track可为对象列表，但是每一个对象必须有_description__描述

    def __call__(self, original_func):
        def _api_func(s1, *arg, **kwargs):
            if self.permission is not None:
                self.permission(s1)
            return original_func(s1, *arg, **kwargs)

        _doc = inspect.getdoc(original_func)
        _description = _doc.split("\n")[0] if _doc else ""
        _api_func.__api_category__ = self.category
        _api_func.__api_name__ = '{}.{}'.format(self.prefix, self.name) if self.prefix else self.name
        _api_func.__api_origin_name__ = original_func.__name__
        _api_func.__api_description__ = _description
        _api_func.__api_doc__ = _doc if _doc else ""
        _api_func.__api_test__ = self.test
        _api_func.__api_track__ = self.track

        return _api_func

    @staticmethod
    def parse_list(_list):
        return _list if isinstance(_list, list) else _list.split(",") if _list else None

    @staticmethod
    def parse_int(_int):
        return 0 if _int is None or _int == '' else int(_int)

    @staticmethod
    def parse_float(_double):
        return 0 if _double is None or _double == '' else float(_double)


open_api = OpenApiDecorate


class Test(object):

    @open_api('employee', name='hello.test')
    def p(self, *args, **kwargs):
        print(args)
        print(kwargs)


def open_api2(name):
    def d(fn):
        @functools.wraps(fn)
        def wrapper(*args, **kwargs):
            print(f'using func:{name}')
            return fn(*args, **kwargs)

        return wrapper

    return d


@open_api2(name='hello')
def do_something():
    print('doing something')


if __name__ == '__main__':
    # hcm_core
    Test().p()
    # self do it
    do_something()
