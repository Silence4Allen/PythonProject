# -*- coding: utf-8 -*-#

# -------------------------------------------------------------------------------
# Name:         main
# Description:  
# Author:       Allen
# Time:         2020/12/14 15:45
# -------------------------------------------------------------------------------
import abc
import subprocess
import sys

if __name__ == '__main__':
    a = subprocess.call([sys.executable, '../../../test_script.py', 'test_text'])
    pass


import abc


class CacheBase(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get(self, key):
        pass

    @abc.abstractmethod
    def set(self, key, value):
        pass
