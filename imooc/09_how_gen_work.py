# -*- coding: utf-8 -*-#

# ------------------------------------------------------------------------------
# Name:         09_how_gen_work
# Description:  
# Author:       Allen
# Time:         2020/12/19 10:58
# ------------------------------------------------------------------------------
import inspect

frame = None


def foo():
    bar()
    # return 'foo'


def bar():
    global frame
    frame = inspect.currentframe()
    # return 'bar'


"""
python.exe（python解释器）会用一个叫做PyEval_EvalFrameEx（c函数）去执行foo函数，首先会创建一个栈桢
python一切皆对象，栈桢也是一个对象，字节码对象
当foo调用子函数bar，又会创建一个栈桢
所有的栈桢都是分配在堆内存（不去释放资源，资源就会一直存在堆内存）上的，这就决定了栈桢可以独立于调用者存在
"""

import dis

print(dis.dis(foo))
foo()
print(frame.f_code.co_name)
caller_frame = frame.f_back
print(caller_frame.f_code.co_name)


def gen_func():
    yield 1
    name = 'bobby'
    yield 2
    age = 30
    return 'imooc'


gen = gen_func()
print(dis.dis(gen))
print(gen.gi_frame.f_lasti)
print(gen.gi_frame.f_locals)
next(gen)
print(gen.gi_frame.f_lasti)
print(gen.gi_frame.f_locals)
next(gen)
print(gen.gi_frame.f_lasti)
print(gen.gi_frame.f_locals)

