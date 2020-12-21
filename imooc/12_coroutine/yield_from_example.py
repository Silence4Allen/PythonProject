# -*- coding: utf-8 -*-#

# ------------------------------------------------------------------------------
# Name:         yield_from_example
# Description:  
# Author:       Allen
# Time:         2020/12/21 15:40
# ------------------------------------------------------------------------------
final_result = {}


def count_sum(p_name):
    total = 0
    nums = []
    while True:
        x = yield
        print("{}销量:{}".format(p_name, x))
        if x == 'stop':
            break
        total += x
        nums.append(x)
    return total, nums


def middle(p_name):
    while True:
        final_result[p_name] = yield from count_sum(p_name)
        print(p_name + "销量统计完成！")


def main():
    data_d = {
        "小霸王": [100, 233, 542, 896],
        "PS4": [1009, 2233, 5442, 8966],
        "Switch": [653, 987, 802, 992]
    }
    for p_name, count_l in data_d.items():
        print("开始统计{}销量".format(p_name))
        m = middle(p_name)
        m.send(None)  # 预激middle协程
        for value in count_l:
            m.send(value)  # 给协程传递每一组的值
        m.send('stop')  # 停止协程
    print("final_result:{}".format(final_result))


if __name__ == '__main__':
    main()
