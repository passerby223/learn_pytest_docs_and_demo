# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time      : 2020/9/23 下午5:14
# @Author    : passerby223
# @FileName  : test_skip_basis.py
# @Description  : 

import pytest


@pytest.fixture(autouse=True)
def login():
    print("====登录====")


def test_case01():
    print("我是测试用例11111")


@pytest.mark.skip(reason="不执行该用例！！因为没写好！！")
def test_case02():
    print("我是测试用例22222")


class Test1:

    def test_1(self):
        print("%% 我是类测试用例1111 %%")

    @pytest.mark.skip(reason="不想执行")
    def test_2(self):
        print("%% 我是类测试用例2222 %%")


@pytest.mark.skip(reason="类也可以跳过不执行")
class TestSkip:
    def test_1(self):
        print("%% 不会执行 %%")


def test_function():
    n = 1
    while True:
        print(f"这是我第{n}条用例")
        n += 1
        if n == 5:
            pytest.skip("我跑五次了不跑了")
