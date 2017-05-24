#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'Kyrix'
__mtime__ = '2017/5/23'
dddd
"""

import os


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
