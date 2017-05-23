#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = 'Pythonpatterns'
__author__ = 'Kyrix'
__mtime__ = '2017/4/19'

"""

import os


# Chain of responsibility
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


# Command
class RenameFileCommand(object):
    def __init__(self, fromfilename, tofilename):
        self._fromfilename = fromfilename
        self._tofilename = tofilename

    def execute(self):
        os.rename(self._fromfilename, self._tofilename)

    def undo(self):
        os.rename(self._tofilename, self._fromfilename)


class History(object):
    def __init__(self):
        self._commands = list()

    def execute(self, command):
        self._commands.append(command)
        command.execute()

    def undo(self):
        self._commands.pop().undo()

history = History()
history.execute(RenameFileCommand('cv1.doc', 'cv2.doc'))
history.execute(RenameFileCommand('cv3.doc', 'cv4.doc'))
history.undo()
history.undo()


#  Singleton
class Singleton(object):
    def __init__(self, singleton):
        self._singleton = singleton

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_singleton'):
            cls._singleton = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._singleton

#  Adapter


#

