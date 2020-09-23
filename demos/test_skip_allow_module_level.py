# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time      : 2020/9/23 下午5:21
# @Author    : passerby223
# @FileName  : test_skip_allow_module_level.py
# @Description  : 当 allow_module_level=True 时，可以设置在模块级别跳过整个模块


import sys
import pytest

if sys.platform.startswith("win"):
    pytest.skip("skipping windows-only tests", allow_module_level=True)


@pytest.fixture(autouse=True)
def login():
    print("====登录====")


def test_case01():
    print("我是测试用例11111")
