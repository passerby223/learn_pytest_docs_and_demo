# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time      : 2020/9/23 下午5:25
# @Author    : passerby223
# @FileName  : test_skipif.py
# @Description  : @pytest.mark.skipif 希望有条件地跳过某些测试用例

import sys
import pytest
from demos.pytest_golbal_skip_marks import skipmark, skipifmark


@pytest.mark.skipif(sys.platform == 'linux', reason="does not run on linux")
class TestSkipIf(object):
    def test_function(self):
        print("不能在Linux上运行")


class TestSkip_Mark(object):

    @skipifmark
    def test_function1(self):
        print("测试标记")

    def test_def(self):
        print("测试标记")


@skipmark
def test_skip():
    print("测试标记")
