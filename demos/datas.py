# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time      : 2020/10/9 下午6:47
# @Author    : passerby223
# @FileName  : datas.py
# @Description  : 

# 增加可读性
data_1 = [
    (1, 2, 3),
    (4, 5, 9)
]

# ids
ids = ["a:{} + b:{} = expect:{}".format(a, b, expect) for a, b, expect in data_1]
if __name__ == '__main__':
    print(ids)
