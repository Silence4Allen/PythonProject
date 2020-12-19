# -*- coding: utf-8 -*-#

# ------------------------------------------------------------------------------
# Name:         09_read_file
# Description:  
# Author:       Allen
# Time:         2020/12/19 11:28
# ------------------------------------------------------------------------------
def myreadlines(f, newline):
    buf = ''
    while True:
        while newline in buf:
            pos = buf.index(newline)
            yield buf[:pos]
            buf = buf[pos + len(newline):]
        chunk = f.read(128)
        if not chunk:  # 文件末尾
            yield buf
            break
        buf += chunk


with open('09_input.txt') as f:
    for line in myreadlines(f, '{|}'):
        print(line)
