# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time      : 2020/9/18 下午4:11
# @Author    : passerby223
# @FileName  : test_02_assert.py
# @Description  : 
import pytest


def f():
    return 3


def test_func():
    a = f()
    assert a % 2 == 0, f"判断a为偶数，当前a的值为{a}"


'''
常用断言
pytest 里面断言实际上就是 python 里面的 assert 断言方法，常用的有以下几种
assert xx ：判断 xx 为真
assert not xx ：判断 xx 不为真
assert a in b ：判断 b 包含 a
assert a == b ：判断 a 等于 b
assert a != b ：判断 a 不等于 b
'''

'''
异常断言
可以使用 pytest.raises 作为上下文管理器，当抛出异常时可以获取到对应的异常实例
'''


def test_division():
    with pytest.raises(ZeroDivisionError):
        1 / 0


# 详细断言异常
def test_zero_division_long():
    with pytest.raises(ZeroDivisionError) as excinfo:
        1 / 0

    # 断言异常类型 type
    assert excinfo.type == ZeroDivisionError
    # 断言异常 value 值
    print(f'\n异常value值：{excinfo.value}')
    print(f'异常traceback值：{excinfo.traceback}')
    assert "division by zero" in str(excinfo.value)
    '''
    excinfo ：是一个异常信息实例
    主要属性： .type 、  .value 、 .traceback 
    注意：断言 type 的时候，异常类型是不需要加引号的，断言 value值的时候需转 str
    '''


# 断言装饰器
@pytest.mark.xfail(raises=ZeroDivisionError)
def test_f():
    1 / 0
