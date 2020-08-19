# -*- coding: utf-8 -*-#

# -------------------------------------------------------------------------------
# Name:         others
# Description:  其他排序
# Author:       Allen
# Time:         2020/8/19 20:14
# -------------------------------------------------------------------------------

if __name__ == '__main__':
    # 将字典按key或value排序
    d = {'a': 24, 'i': 52, 'c': 12, 'k': 33}
    print('d = {}'.format(d))
    d1 = sorted(d.items(), key=lambda x: x[0])  # 按照key排序
    print('按照key排序, d1 = {}'.format(d1))
    d2 = sorted(d.items(), key=lambda x: x[1])  # 按照value排序
    print('按照value排序,d2 = {}'.format(d2))
