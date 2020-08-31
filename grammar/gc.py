# -*- coding: utf-8 -*-#

# -------------------------------------------------------------------------------
# Name:         gc
# Description:  可查看：https://www.jianshu.com/p/ef8a218c6b89
# Author:       Allen
# Time:         2020/8/20 19:53
# -------------------------------------------------------------------------------
import sys
import objgraph
import gc

if __name__ == '__main__':
    class Person:
        pass


    class Dog:
        pass


    p = Person()
    d = Dog()

    p.pet = d
    d.master = p

    print(sys.getrefcount(p))
    print(sys.getrefcount(d))

    del p
    del d

    gc.collect()  # 手动触发垃圾回收

    print(objgraph.count("Person"))
    print(objgraph.count("Dog"))
