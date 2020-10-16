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
import time

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])


@click.group(context_settings=CONTEXT_SETTINGS)
@click.version_option(version='1.0.0')
def cli():
    pass


@cli.command()
@click.option('--count', default=1, help='问候的次数')
@click.option('--name', prompt='你的名字', help='问候的名字')
@click.option('--t', default='y', required=True,
              type=click.Choice(['y', 'n']),
              prompt='打印当前时间戳',
              help='打印时间戳')
def hello(count, name, t):
    """
    简单的问候名字次数程序
    :param count: 问候的次数
    :param name: 问候的名字
    :param t: 是否打印当前时间戳
    :return: None
    """
    for x in range(count):
        click.echo('你好 %s!' % name)
    if t == 'y':
        print(time.time())

    return None


@cli.command(context_settings=CONTEXT_SETTINGS)
@click.argument('a', type=int, required=True)
@click.argument('b', type=int, required=True)
def add(a, b):
    """
    两数相加
    :param a: 加数
    :param b: 被加数
    :return: 结果
    """
    click.echo(click.style('%s+%s=' % (a, b), fg='green', bold=True))
    print(a + b)
    return a + b


if __name__ == '__main__':
    cli()
