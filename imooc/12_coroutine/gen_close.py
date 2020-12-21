# -*- coding: utf-8 -*-#

# ------------------------------------------------------------------------------
# Name:         gen_close
# Description:  
# Author:       Allen
# Time:         2020/12/21 15:09
# ------------------------------------------------------------------------------
def gen_func():
    yield "http://www.baidu.com"
    yield 2
    yield 3
    return "allen"


if __name__ == '__main__':
    gen = gen_func()
    print(next(gen))
    gen.close()
    print(next(gen))
