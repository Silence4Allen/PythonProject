# -*- coding: utf-8 -*-#

# ------------------------------------------------------------------------------
# Name:         new_init
# Description:  
# Author:       Allen
# Time:         2020/12/18 13:22
# ------------------------------------------------------------------------------

"""
new是用来控制对象生成的，在对象生成之前
init是用来完善对象属性的，对象此时已经生成
如果new不返回对象，则不会调用init方法
"""


class User:
    def __new__(cls, *args, **kwargs):
        print('new')
        return super().__new__(cls)

    def __init__(self, name):
        print('init')
        self.name = name


if __name__ == '__main__':
    user = User('allen')
