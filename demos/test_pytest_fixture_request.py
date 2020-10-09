# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time      : 2020/10/9 下午6:53
# @Author    : passerby223
# @FileName  : test_pytest_fixture_request.py
# @Description  : 

# 传单个参数
import pytest


@pytest.fixture()
def login(request):
    name = request.param
    print(f"== 账号是：{name} ==")
    return name


data = ["pyy1", "polo"]
ids = [f"login_test_name is:{name}" for name in data]


@pytest.mark.parametrize("login", data, ids=ids, indirect=True)
def test_name(login):
    print(f" 测试用例的登录账号是：{login} ")
