# -*- coding: utf-8 -*-#

# -------------------------------------------------------------------------------
# Name:         callback
# Description:  回调函数：https://www.zhihu.com/question/19801131
# Author:       Allen
# Time:         2020/8/31 20:01
# -------------------------------------------------------------------------------


class Transport:
    def bicycle(self, goods):
        print(f'this is a bicycle with {goods}')

    def car(self, goods):
        print(f'this is a car with {goods}')

    def airplane(self, goods):
        print(f'this is a airplane with {goods}')


if __name__ == '__main__':
    t = Transport()


    def seller(transport_method, goods):
        print(f'this is seller, and using {transport_method.__name__} to transfer {goods}')
        transport_method(goods)


    seller(t.car, '鞋子')
