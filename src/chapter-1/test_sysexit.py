#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import pytest


def f():
    # 解释器请求退出
    raise SystemExit(1)


def test_mytest():
    with pytest.raises(SystemExit):
        f()
