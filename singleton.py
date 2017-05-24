#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'Kyrix'
__mtime__ = '2017/5/24'

"""

class Singleton(object):
    def __init__(self, singleton):
        self._singleton = singleton

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_singleton'):
            cls._singleton = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._singleton