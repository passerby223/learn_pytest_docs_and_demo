# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time      : 2020/10/10 下午12:18
# @Author    : passerby223
# @FileName  : conftest.py
# @Description  : 

import pytest


@pytest.fixture(scope="module")
def open_51(login):
    name, token = login
    print(f"###用户 {name} 打开51job网站###")
