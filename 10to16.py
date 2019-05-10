#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2019 miffyrcee <miffyrcee@localhost.localdomain>
#
# Distributed under terms of the MIT license.
"""

"""
hexnum = 115104101108108116101114123108101971141101051101039510111099111100101125


def toList(value):
    return list(str(value))


def is2or3(value):
    if int(value[0] + value[1]) > 50:
        return 0
    else:
        return 1


def remove2or3(value):
    def removeNValue(value, n):
        for i in range(n):
            value.reverse()
            value.pop()
            value.reverse()
        return value

    if (is2or3):
        return removeNValue(value, 3)
    else:
        return removeNValue(value, 2)


def echoNvalue(value):
    if (is2or3):
        return value[0:3]
    else:
        return value[0:2]


def int16(value, base=16):
    return int(str(value), base)


def main():
    value = toList(hexnum)
    hexStoreMachine = ''
    while (len(value) > 2):
        hexStoreMachine += str(int16(''.join(echoNvalue(value))))
        value = remove2or3(value)
    print(hexStoreMachine)
    print(int('474f20414845414420414e4420435241434b204954'))


if __name__ == "__main__":
    main()
