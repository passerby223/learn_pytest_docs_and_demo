# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time      : 2020/10/9 下午1:02
# @Author    : passerby223
# @FileName  : test_pytest_mark_parametrize.py
# @Description  : 

import pytest

data_1 = [(1, 2, 3), (2, 3, 5), (3, 4, 6)]


@pytest.mark.parametrize('a, b, expect', data_1)
class TestParametrize:

    def test_parametrize_1(self, a, b, expect):
        print('\n测试函数11111 测试数据为\n{}-{}'.format(a, b))
        assert a + b == expect

    def test_parametrize_2(self, a, b, expect):
        print('\n测试函数22222 测试数据为\n{}-{}'.format(a, b))
        assert a + b == expect

# @pytest.mark.parametrize("test_input,expected", [("3+5", 8), ("2+4", 6), ("6*9", 42)])
# def test_eval(test_input, expected):
#     print(f"测试数据{test_input},期望结果{expected}")
#     assert eval(test_input) == expected
