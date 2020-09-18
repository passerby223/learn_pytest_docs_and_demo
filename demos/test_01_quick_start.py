# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time      : 2020/9/18 下午2:51
# @Author    : passerby223
# @FileName  : test_01_quick_start.py
# @Description  : 

def func(x):
    return x + 1


def test_answer():
    assert func(3) == 5


class TestClass:
    def test_one(self):
        x = 'this'
        assert 's' in x

    def test_two(self):
        x = 'hello'
        assert hasattr(x, 'check')
'''
如果只执行 pytest ，会查找当前目录及其子目录下以  test_*.py  或 *_test.py 文件，找到文件后，在文件中找到以  test 开头函数并执行
如果只想执行某个文件，可以 pytest start.py 
加上-q，就是显示简单的结果： pytest -q start.py 
'''
'''
Pytest用例的设计原则
用Pytest写用例时候，一定要按照下面的规则去写，否则不符合规则的测试用例是不会执行的
文件名以 test_*.py 文件和*_test.py
以  test_ 开头的函数
以  Test 开头的类，不能包含 __init__ 方法
以  test_ 开头的类里面的方法
所有的包 pakege 必项要有__init__.py 文件
'''

