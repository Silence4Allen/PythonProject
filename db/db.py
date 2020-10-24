# -*- coding: utf-8 -*-#

# -------------------------------------------------------------------------------
# Name:         db
# Description:  
# Author:       Allen
# Time:         2020/10/20 20:39
# -------------------------------------------------------------------------------
import pymysql

if __name__ == '__main__':
    db = pymysql.connect(**{
        'host': "127.0.0.1",
        'user': 'root',
        'password': 'silence4allen',
        'database': 'test',
        'port': 3306
    })
    print(db)

    pass
