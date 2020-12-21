# -*- coding: utf-8 -*-#

# ------------------------------------------------------------------------------
# Name:         coroutine_test
# Description:  
# Author:       Allen
# Time:         2020/12/21 13:46
# ------------------------------------------------------------------------------
def gen_func():
    html = yield "http://www.baidu.com"
    print(html)
    yield 22
    return "allen"


if __name__ == '__main__':
    gen = gen_func()
    # 在调用send发送非None值之前，我们必须启动一次生成器
    # a、gen.send(None)
    # b、next(gen)
    url = gen.send(None)
    html = 'this is a test'
    print(gen.send(html))
