# -*- coding: utf-8 -*-#

# ------------------------------------------------------------------------------
# Name:         yield_from_test
# Description:  
# Author:       Allen
# Time:         2020/12/21 15:21
# ------------------------------------------------------------------------------
from itertools import chain

my_list = [1, 2, 3]
my_dict = {
    "bobby1": "http://www.baid.com",
    "bobby2": "http://www.qq.com"
}
for value in chain(my_list, my_dict, range(5, 10)):
    print(value)


def my_chain(*args, **kwargs):
    print(args)
    for my_iterable in args:
        print(my_iterable)
        for value in my_iterable:
            yield value


# yield from iterable
def my_chain2(*args, **kwargs):
    for my_iterable in args:
        yield from my_iterable
        # for value in my_iterable:
        #     yield value


for value in my_chain2(my_list, my_dict, range(5, 10)):
    print(value)
