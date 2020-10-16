#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
@File  : t1.py
@Author: HappyLay
@Date  : 2020/10/17 00:21
@Desc  : 安徽理工大学
"""
__author__ = 'HappyLay'

from math import sqrt, pow
from decimal import Decimal


# x2 - 10x +16 = 0

# 参数
# a, b, c = 1, -10, 16

def equation(a, b, c):
    """
    计算二元一次方程
    :param a: 一次项系数
    :param b: 二次型系数
    :param c: 常数
    :return:
    """
    x1 = None
    x2 = None
    # 通项公式
    dt = pow(b, 2) - 4 * a * c

    # 判断解的情况
    if dt == 0:
        x1 = x2 = (-b + sqrt(dt)) / (2 * a)
        print('相同解：', x1)
    elif dt > 0:
        x1 = (-b + sqrt(dt)) / (2 * a)
        x2 = (-b - sqrt(dt)) / (2 * a)
        print('不同解：', x1, x2)
    else:
        print('无解')

    return x1, x2


if __name__ == '__main__':
    # 精度丢失
    print(0.3 - 0.1)

    print(Decimal('0.3') - Decimal('0.1'))

    x3 = x4 = 1
    print(x3, x4)

    x1, x2 = equation(1, 4, -12)
    print(x1, x2)
