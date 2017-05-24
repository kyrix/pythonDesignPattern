#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = 'Pythonpatterns'
__author__ = 'Kyrix'
__mtime__ = '2017/4/19'

"""


class SomeAnimals(object):
    def __init__(self, habits=None):
        self._habits = list()
        if habits is not None:
            self._habits += habits

    def showhabits(self, content):
        for habit in self._habits:
            content = habit(content)
        return content


def deleta(some):
    # print "I'am %s" % (%self)
    return some.replace('a', '')


def deletb(some):
    return some.replace('b', '')


def deletc(some):
    return some.replace('c', '')

animal = SomeAnimals([deleta, deletb, deletc])
print animal.showhabits('ffdafdasqfdccccfdsa')


