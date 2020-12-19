# -*- coding: utf-8 -*-#

# ------------------------------------------------------------------------------
# Name:         attr_desc
# Description:  
# Author:       Allen
# Time:         2020/12/18 10:32
# ------------------------------------------------------------------------------
"""
如果user是某个类的实例，那么user.age（以及等价的getattr(user, 'age')）
首先调用__getattribute__。如果类定义了__getattr__方法，
那么在__getattribute__抛出AttributeError的时候就会调用到__getattr__，
而对于描述符（__get__）的调用，则是发生在__getattribute__内部的。
user = User()，那么user.age顺序如下：
1.如果'age'是出现在User或其他基类的__dict__中，且age是data_descriptor，那么调用其__get__方法。否则
2.如果'age'出现在user的__dict__中，那么直接返回user.__dict__['age']。否则
3.如果'age'出现在User或其基类的__dict__中
    a.如果age是non-data descriptor，那么调用其__get__方法，否则b
    b.返回__dict__['age']
4.如果User有__getattr__方法，调用__getattr__方法。否则
5.抛出AttributeError
"""
import numbers


# 属性描述符
class IntField(object):
    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        if not isinstance(value, numbers.Integral):
            raise ValueError("int value need")
        self.value = value

    def __delete__(self, instance):
        del self.value


class User:
    # age = IntField()
    pass


if __name__ == '__main__':
    user = User()
    user.age = 30
    print(user.__dict__)
    user.__dict__.update({'age': 10})
    print(user.__dict__)
    print(user.age)
