#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2019 miffyrcee <miffyrcee@localhost.localdomain>
#
# Distributed under terms of the MIT license.
"""
cipherShift
"""

import getopt
import sys


def shiftLength(character, length):
    if (ord(character) == 32):
        return 11
    else:
        if (ord(character) + length > 90):
            return length - 26
        else:
            return length


def main():
    sourceValue = 'OHJRPUNPZNYLHA'
    for i in range(1, 26):
        unciperStoreMachine = ''
        for j in sourceValue:
            unciperStoreMachine += chr(ord(j) + shiftLength(j, i))
        print(unciperStoreMachine)


if __name__ == '__main__':
    main()
