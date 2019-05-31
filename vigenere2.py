#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2019 miffyrcee <miffyrcee@localhost.localdomain>
#
# Distributed under terms of the MIT license.
"""

"""
import re
import string
import time

import numpy


class vigenere(object):
    @property
    def vigenereArray(self):
        _varray = numpy.zeros((26, 26), int)
        for i in range(0, 26):
            for j in range(0, 26):
                _varray[i][j] = (i + j) % 26
        return _varray

    def shiftCircle(self, cipheredText, length):
        _carray = []
        for i in self.toNumber(cipheredText):
            _carray.append((length + i) % 26)
        return self.toString(_carray)

    def toNumber(self, cipheredText):
        _carray = []
        for i in cipheredText:
            _carray.append(ord(i) - 65)
        return _carray

    def toString(self, cipheredText):
        _carray = ''
        for i in cipheredText:
            _carray += chr(i + 65)
        return _carray

    def decipher(self, cipheredText, length):
        pass

    def splitText(self, cipheredText, length):
        _pattern = '.{1,'
        _pattern += str(length)
        _pattern += '}'
        return re.findall(_pattern, cipheredText)

    def _POL(self):
        _fol = [
            8.167, 1.492, 2.782, 4.253, 12.702, 2.228, 2.015, 6.094, 6.966,
            0.153, 0.772, 4.025, 2.406, 6.749, 7.507, 1.929, 0.095, 5.987,
            6.327, 9.056, 2.758, 0.978, 2.360, 0.150, 1.974, 0.074
        ]
        return _fol

    def ic(self, cipheredText):
        lastTime = time.time()

        _possAverage = []
        for n in range(1, len(cipheredText)):
            #  for n in range(9, 10):
            _possArray = []
            for i in self.splitText(cipheredText, n):
                _poss = 0
                for j in string.ascii_uppercase:
                    _poss += pow((i.count(j) / len(i)), 2)
                _possArray.append(_poss)
            #  print(_possArray)
            _possAverage.append((numpy.average(_possArray), n))
        print(time.time() - lastTime)
        return _possAverage


def main():
    v = vigenere()
    #  for i in range(1, 16):
    #  for j in range(1, i):
    #  print(v.ic(v.shiftCircle('DLECYBRXNPKPYXVVOPXSDAICDAIC', j), i), i)
    print(v.ic('ABCDEABCDEABCDEABC'))
if __name__ == '__main__':
    main()
