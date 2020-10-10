# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time      : 2020/10/10 下午12:18
# @Author    : passerby223
# @FileName  : test_case1.py
# @Description  : 

from time import sleep

import pytest


@pytest.mark.parametrize("n", list(range(5)))
def test_case2_01(open_51, n):
    sleep(1)
    print("51job，列出所有职位用例", n)


@pytest.mark.parametrize("n", list(range(5)))
def test_case2_02(open_51, n):
    sleep(1)
    print("51job，找出所有python岗位", n)
