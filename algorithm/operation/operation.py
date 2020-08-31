# -*- coding: utf-8 -*-#

# -------------------------------------------------------------------------------
# Name:         operation
# Description:  
# Author:       Allen
# Time:         2020/8/19 20:50
# -------------------------------------------------------------------------------
if __name__ == '__main__':
    a = ['lily', 'amy', 'jack']
    b = ['bob', 'amy', 'zev']
    print(set(a) & set(b))  # 交集
    print(set(a) ^ set(b))  # 差集
    print(set(a) | set(b))  # 并集
