# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time      : 2020/10/10 下午12:18
# @Author    : passerby223
# @FileName  : conftest.py
# @Description  :

import pytest


# 外层conftest.py

@pytest.fixture(scope="session")
def login():
    print("====登录功能，返回账号，token===")
    name = "testyy"
    token = "npoi213bn4"
    yield name, token
    print("====退出登录！！！====")
