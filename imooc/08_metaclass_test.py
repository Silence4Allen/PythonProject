# -*- coding: utf-8 -*-#

# ------------------------------------------------------------------------------
# Name:         metaclass_test
# Description:  
# Author:       Allen
# Time:         2020/12/18 13:28
# ------------------------------------------------------------------------------
"""
 1.类也是对象，type是创建类的类
 2.什么是元类？？？
   元类就是创建类的类，元类type->class（对象）->对象
 3.python中类的实例化过程
   会首先寻找metaclass，通过metaclass去创建类对象
"""
from collections.abc import *

class MetaClass(type):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls, *args, **kwargs)

    pass


class User(metaclass=MetaClass):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


if __name__ == '__main__':
    Student = type('Student', (object,), {"name": "allen"})
    student = Student()
    print(student.name)

    user = User('allen')
    print(user)
