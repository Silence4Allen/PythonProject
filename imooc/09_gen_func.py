# -*- coding: utf-8 -*-#

# ------------------------------------------------------------------------------
# Name:         gen_func
# Description:  
# Author:       Allen
# Time:         2020/12/18 16:58
# ------------------------------------------------------------------------------
"""
生成器函数，函数里面只要有yield关键字
"""


# 0、1、1、2、3、5、8、13
def fibo1(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    else:
        return fibo1(n - 1) + fibo1(n - 2)


def fibo2(n):
    count, a, b = 0, 0, 1
    while count < n:
        yield a
        count += 1
        a, b = b, a + b


if __name__ == '__main__':
    print(fibo1(8))
    for i in fibo2(8):
        print(i)
