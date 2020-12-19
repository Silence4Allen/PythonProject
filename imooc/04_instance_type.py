# -*- coding: utf-8 -*-#

# ------------------------------------------------------------------------------
# Name:         instance_type
# Description:  
# Author:       Allen
# Time:         2020/12/15 15:42
# ------------------------------------------------------------------------------
class A:
    pass


class B(A):
    pass


b = B()
print(isinstance(b, B))
print(isinstance(b, A))
print(type(b) is B)
print(type(b) is A)
