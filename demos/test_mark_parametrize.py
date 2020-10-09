# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time      : 2020/10/9 下午1:19
# @Author    : passerby223
# @FileName  : test_mark_parametrize.py.py
# @Description  :

import pytest

# 笛卡尔积，组合数据
# data_1 = [1, 2, 3]
# data_2 = ['a', 'b']
# 
# 
# @pytest.mark.parametrize('a', data_1)
# @pytest.mark.parametrize('b', data_2)
# def test_parametrize_1(a, b):
#     print(f'笛卡尔积 测试数据为 ： {a}，{b}')

# 参数化 ，传入字典数据
# 字典
# data_3 = (
#     {
#         'user': 1,
#         'pwd': 2
#     },
#     {
#         'user': 3,
#         'pwd': 4
#     }
# )
# 
# 
# @pytest.mark.parametrize('dic', data_3)
# def test_parametrize_1(dic):
#     print(f'测试数据为\n{dic}')
#     print(f'user:{dic["user"]},pwd:{dic["pwd"]}')


# 标记参数化
# @pytest.mark.parametrize("test_input,expected", [
#     ("3+5", 8),
#     ("2+4", 6),
#     pytest.param("6 * 9", 42, marks=pytest.mark.xfail),
#     pytest.param("6*6", 42, marks=pytest.mark.skip)
# ])
# def test_mark(test_input, expected):
#     assert eval(test_input) == expected

# 增加可读性
data_1 = [
    (1, 2, 3),
    (4, 5, 9)
]

# ids
ids = ["a:{} + b:{} = expect:{}".format(a, b, expect) for a, b, expect in data_1]


@pytest.mark.parametrize('a, b, expect', data_1, ids=ids)
class TestParametrize(object):

    def test_parametrize_1(self, a, b, expect):
        print('测试函数1测试数据为{}-{}'.format(a, b))
        assert a + b == expect

    def test_parametrize_2(self, a, b, expect):
        print('测试函数2数据为{}-{}'.format(a, b))
        assert a + b == expect
