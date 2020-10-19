#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Gregorio Ambrosio"
__contact__ = "gambrosio[at]uma.es"
__copyright__ = "Copyright 2020, Gregorio Ambrosio"
__date__ = "2020/10/12"
__license__ = "MIT"

#import robotathome
from robotathome import dataset


print("Hello")
rhds = dataset.Dataset("MyRobot@Home")

print(rhds.name)

