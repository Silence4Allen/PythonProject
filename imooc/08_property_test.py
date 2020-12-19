# -*- coding: utf-8 -*-#

# ------------------------------------------------------------------------------
# Name:         property_test
# Description:  
# Author:       Allen
# Time:         2020/12/17 21:11
# ------------------------------------------------------------------------------
from datetime import datetime, date


class User(object):
    def __init__(self, name, birthday):
        self.name = name
        self.birthday = birthday
        self._age = 0

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._age = value


if __name__ == '__main__':
    user = User('allen', date(year=1994, month=2, day=18))
    print(user.age)
    user.age = 30
    print(user.age)
