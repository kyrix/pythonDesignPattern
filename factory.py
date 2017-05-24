#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'Kyrix'
__mtime__ = '2017/5/24'

"""


class GreekGetter:
    """A simple localizer a   dddla get text"""
    def __init__(self):
        self.trans = dict(dog="蟽魏蠉位慰蟼", cat="纬维蟿伪")

    def getby(self, msgid):
        """We'll punt if we don't have a translation"""
        try:
            return self.trans[msgid]
        except KeyError:
            return str(msgid)


class EnglishGetter:
    """Simply echoes the msg ids"""
    def getby(self, msgid):
        return str(msgid)


def get_localizer(language="English"):
    """The factory method"""
    languages = dict(English=EnglishGetter, Greek=GreekGetter)
    return languages[language]()

# Create our localizers
e, g = get_localizer("English"), get_localizer("Greek")
# Localize some text
for msgid in "dog parrot cat bear".split():
    print(e.getby(msgid), g.getby(msgid))