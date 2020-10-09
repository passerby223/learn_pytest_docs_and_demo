# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time      : 2020/10/9 下午12:06
# @Author    : passerby223
# @FileName  : test_pytest_mark.py
# @Description  : 

import pytest


@pytest.mark.weibo
def test_weibo():
    print("测试微博")


@pytest.mark.toutiao
def test_toutiao():
    print("测试头条")


@pytest.mark.toutiao
def test_toutiao1():
    print("再次测试头条")


@pytest.mark.xinlang
class TestClass:
    def test_method(self):
        print("测试新浪")


def testnoMark():
    print("没有标记测试")
