# -*- coding: utf-8 -*-#

# -------------------------------------------------------------------------------
# Name:         iterator_and_generator
# Description:  
# Author:       Allen
# Time:         2020/9/14 19:45
# -------------------------------------------------------------------------------
class Iterator(object):
    l = []

    def __next__(self, p):
        if len(self.l) >= p:
            return self.l[p + 1]

    def __iter__(self):
        pass
