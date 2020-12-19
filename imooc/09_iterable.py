# -*- coding: utf-8 -*-#

# ------------------------------------------------------------------------------
# Name:         iterable
# Description:  
# Author:       Allen
# Time:         2020/12/18 16:45
# ------------------------------------------------------------------------------
"""
什么是迭代协议？
迭代器是什么？？迭代器是访问集合内元素的一种方式，一般用来遍历数据
迭代器和以下标的访问方式不一样，迭代器是不能返回的
迭代器提供了一种惰性方式数据的方法
"""
from collections.abc import Iterable, Iterator

a = [1, 2]
print(isinstance(a, Iterable))
print(isinstance(a, Iterator))
iter_a = iter(a)
print(isinstance(iter_a, Iterable))
print(isinstance(iter_a, Iterator))
