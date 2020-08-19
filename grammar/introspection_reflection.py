# -*- coding: utf-8 -*-#

# -------------------------------------------------------------------------------
# Name:         introspection_reflection
# Description:  
# Author:       Allen
# Time:         2020/8/18 20:11
# -------------------------------------------------------------------------------


class Cat(object):  # 类，Cat指向这个类对象
    def __init__(self, name='kitty'):
        self.name = name

    def sayHi(self, msg):  # 实例方法，sayHi指向这个方法对象，使用类或实例.sayHi访问
        msg = msg or 'says Hi!'
        print(self.name, msg)  # 访问名为name的字段，使用实例.name访问


if __name__ == '__main__':
    cat = Cat()
    name = getattr(cat, 'name')
    print(name)
    sex = getattr(cat, 'sex') if hasattr(cat, 'sex') else setattr(cat, 'sex', 'male')
    print(sex)
    print(cat.sex)
    if hasattr(cat, 'sayHi'):
        say = getattr(cat, 'sayHi')
        say("is my name")
