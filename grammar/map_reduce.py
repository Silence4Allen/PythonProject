# -*- coding: utf-8 -*-#

# -------------------------------------------------------------------------------
# Name:         map_reduce
# Description:  map\reduce函数区别：https://www.cnblogs.com/lisa2016/p/11250135.html
# Author:       Allen
# Time:         2020/8/31 18:40
# -------------------------------------------------------------------------------
import sys
from functools import reduce

if __name__ == '__main__':
    def f1(i):
        return i + 1


    def f2(i, j):
        return i + j


    a = [1, 2, 3]
    r1 = list(map(f1, a))
    r2 = reduce(f2, a)
    print(f'r1:{r1},r2:{r2}')

    r2 = reduce(f2, a)
    print(f'r1:{r1},r2:{r2}')
    print(sys.getrecursionlimit())
