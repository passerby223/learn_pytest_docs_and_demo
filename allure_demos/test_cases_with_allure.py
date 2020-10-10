# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time      : 2020/10/10 下午1:19
# @Author    : passerby223
# @FileName  : test_cases_with_allure.py
# @Description  : 

import pytest


def test_success():
    """this test succeeds"""
    assert True


def test_failure():
    """this test fails"""
    assert False


def test_skip():
    """this test is skipped"""
    pytest.skip('for a reason!')


def test_broken():
    raise Exception('oops')
