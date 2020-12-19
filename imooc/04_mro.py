# -*- coding: utf-8 -*-#

# ------------------------------------------------------------------------------
# Name:         mro
# Description:  
# Author:       Allen
# Time:         2020/12/15 17:02
# ------------------------------------------------------------------------------
class A:
    def __init__(self):
        print('A')


class B(A):
    def __init__(self):
        print('B')
        super().__init__()


class C():
    def __init__(self):
        print('C')
        super().__init__()


class D(B, C):
    def __init__(self):
        print('D')
        super().__init__()


if __name__ == '__main__':
    d = D()
    print(D.__mro__)
