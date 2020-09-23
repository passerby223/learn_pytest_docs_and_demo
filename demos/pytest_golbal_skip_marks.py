# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time      : 2020/9/23 下午5:29
# @Author    : passerby223
# @FileName  : pytest_golbal_skip_marks.py
# @Description  : 

import sys
import pytest

skipmark = pytest.mark.skip(reason="不能在Linux上运行=====")
skipifmark = pytest.mark.skipif(sys.platform == 'linux', reason="不能在linux上运行啦啦啦=====")
