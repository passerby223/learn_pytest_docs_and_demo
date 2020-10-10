# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time      : 2020/10/10 下午12:19
# @Author    : passerby223
# @FileName  : test_case2.py
# @Description  : 

from time import sleep

import pytest


@pytest.mark.parametrize("n", list(range(5)))
def test_no_fixture(login, n):
    sleep(1)
    print("==没有__init__测试用例，我进入头条了==", login)
