# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time      : 2020/10/9 下午6:53
# @Author    : passerby223
# @FileName  : test_pytest_fixture_request.py
# @Description  : 

import pytest
# 案例一：传单个参数
# 
# 
# @pytest.fixture()
# def login(request):
#     name = request.param
#     print(f"== 账号是：{name} ==")
#     return name
# 
# 
# data = ["pyy1", "polo"]
# ids = [f"login_test_name is:{name}" for name in data]
# 
# 
# # 添加  indirect=True  参数是为了把 login 当成一个函数去执行，而不是一个参数，并且将data当做参数传入函数
# @pytest.mark.parametrize("login", data, ids=ids, indirect=True)
# # def test_name(login) ，这里的login是获取fixture返回的值
# def test_name(login):
#     print(f" 测试用例的登录账号是：{login} ")
# 
# 
# # 案例二：传多个参数
# @pytest.fixture()
# def logins(request):
#     param = request.param
#     print(f"账号：{param['username']}，密码：{param['pwd']}")
#     return param
# 
# 
# data = [
#     {"username": "name1", "pwd": "pwd1"},
#     {"username": "name2", "pwd": "pwd2"},
# ]
# 
# 
# @pytest.mark.parametrize("logins", data, indirect=True)
# def test_name_pwd(logins):
#     print(f"账号是：{logins['username']}，密码是：{logins['pwd']}")
# 
# 
# # 案例三：多个fixture（只加一个装饰器）
# # 多个fixture
# @pytest.fixture(scope="module")
# def input_user(request):
#     user = request.param
#     print("登录账户：%s" % user)
#     return user
# 
# 
# @pytest.fixture(scope="module")
# def input_psw(request):
#     psw = request.param
#     print("登录密码：%s" % psw)
#     return psw
# 
# 
# data = [
#     ("name1", "pwd1"),
#     ("name2", "pwd2")
# ]
# 
# 
# @pytest.mark.parametrize("input_user,input_psw", data, indirect=True)
# def test_more_fixture(input_user, input_psw):
#     print("fixture返回的内容:", input_user, input_psw)


# 案例四：多个fixture（叠加装饰器）
# 多个fixture
@pytest.fixture(scope="function")
def input_user(request):
    user = request.param
    print("登录账户：%s" % user)
    return user


@pytest.fixture(scope="function")
def input_psw(request):
    psw = request.param
    print("登录密码：%s" % psw)
    return psw


name = ["name1", "name2"]
pwd = ["pwd1", "pwd2"]


@pytest.mark.parametrize("input_user", name, indirect=True)
@pytest.mark.parametrize("input_psw", pwd, indirect=True)
def test_more_fixture(input_user, input_psw):
    print("fixture返回的内容:", input_user, input_psw)
