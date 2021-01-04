# -*- coding: utf-8 -*-#

# -------------------------------------------------------------------------------
# Name:         test
# Description:  
# Author:       Allen
# Time:         2020/9/14 19:21
# -------------------------------------------------------------------------------

import logging


def get_dynamic_script_content():
    _dynamic_script_content = ""
    with open("dynamic_script_demo.txt", "r") as fs:
        _lines = fs.readlines()
        for _l in _lines:
            _dynamic_script_content += _l

    return _dynamic_script_content


if __name__ == '__main__':
    dynamic_script_content = get_dynamic_script_content()
    import_class_dict = {k: v for k, v in list(globals().items()) if
                         k not in ['self', 'get_dynamic_script_content', dynamic_script_content] and not k.startswith(
                             "_")}

    # 加载云函数之前保存一下当前全局变量
    origin_keys = list(import_class_dict.keys())

    # 加载云函数，此时会在import_class_dict中加载云函数中的类和全局变量
    exec(dynamic_script_content, import_class_dict)

    # 筛选出新加载的类对象
    classes = [v for k, v in import_class_dict.items() if k not in origin_keys and not k.startswith("_")]
    a = classes[0]().text
    print(a)

