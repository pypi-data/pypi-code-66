#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
@File  : hello.py
@Author: HappyLay
@Date  : 2020/10/16 16:22
@Desc  : 安徽理工大学
"""
__author__ = 'HappyLay'

import click


@click.command()
@click.option('--count', default=1, help='问候的次数')
@click.option('--name', prompt='你的名字', help='问候的名字')
def hello(count, name):
    """简单的问候名字次数程序"""
    for x in range(count):
        click.echo('Hello %s!' % name)


if __name__ == '__main__':
    hello()
