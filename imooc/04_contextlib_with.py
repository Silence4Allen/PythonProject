# -*- coding: utf-8 -*-#

# ------------------------------------------------------------------------------
# Name:         contextlib_with
# Description:  
# Author:       Allen
# Time:         2020/12/15 17:30
# ------------------------------------------------------------------------------
from contextlib import contextmanager


# try except finally
# 第一种处理资源的方法
@contextmanager
def file_open(file_name):
    print("open file")
    yield {}
    print("close file")


with file_open("test.txt")as f_opened:
    print("file processing")


# 第二种处理资源的方法
class Handle:
    def __enter__(self):
        print("enter")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("exit")

    def do_sth(self):
        print("doing...")


with Handle() as handle:
    handle.do_sth()
