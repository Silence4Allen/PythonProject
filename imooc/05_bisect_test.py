# -*- coding: utf-8 -*-#

# ------------------------------------------------------------------------------
# Name:         bisect
# Description:  
# Author:       Allen
# Time:         2020/12/17 13:40
# ------------------------------------------------------------------------------
import bisect

# 用来处理已排序的序列，用来维持已排序的序列，升序
# 二分查找
l = []
bisect.insort(l, 3)
bisect.insort(l, 1)
bisect.insort(l, 5)
bisect.insort(l, 4)
bisect.insort(l, 2)
print(l)
# 该函数返回插入值的位置，但是并不会插入
print(bisect.bisect(l, 8))
# 该函数返回插入值的位置，但是并不会插入；如果有重复值，插在重复值左边
print(bisect.bisect_left(l, 1))
# 该函数返回插入值的位置，但是并不会插入；如果有重复值，插在重复值右边
print(bisect.bisect_right(l, 1))
# 该函数插入值，如果有重复值，插在重复值左边
bisect.insort_left(l, 2)
print(l)
# 该函数插入值，如果有重复值，插在重复值右边
bisect.insort_right(l, 2)
print(l)
