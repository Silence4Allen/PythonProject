# -*- coding: utf-8 -*-#

# ------------------------------------------------------------------------------
# Name:         getattr
# Description:  
# Author:       Allen
# Time:         2020/12/17 21:17
# ------------------------------------------------------------------------------
# __getattr__：就是在查找不到属性的时候调用
# __getattribute__：这个更高级，只要是获取对象属性，就会进该魔法函数。其实这个魔法函数中调用了__getattr__，所以不建议复写

class User:
    def __init__(self, info={}):
        self.info = info

    def __getattr__(self, item):
        return self.info[item]

    # def __getattribute__(self, item):
    #     return 'allen'


if __name__ == '__main__':
    user = User(info={"company_name": "inspur", "name": "allen", "age": 10})
    print(user.name)
    print(user.age)
