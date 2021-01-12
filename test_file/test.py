# -*- coding: utf-8 -*-#

# ------------------------------------------------------------------------------
# Name:         test.py
# Description:  
# Author:       Allen
# Time:         2021/1/12 10:42
# ------------------------------------------------------------------------------

from test_file.celery_task import add

if __name__ == '__main__':
    print('start')
    res = add.delay(2, 14)
    print('end')
    print(res)
