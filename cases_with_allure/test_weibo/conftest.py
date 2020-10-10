# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time      : 2020/10/10 下午12:19
# @Author    : passerby223
# @FileName  : conftest.py
# @Description  : 

import pytest


@pytest.fixture(scope="function")
def open_weibo(login):
    name, token = login
    print(f"&&& 用户 {name} 返回微博首页 &&&")
