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

import numpy


class vigenere(object):
    @property
    def vigenereArray(self):
        _varray = numpy.zeros((26, 26), int)
        for i in range(0, 26):
            for j in range(0, 26):
                _varray[i][j] = (i + j) % 26
        return _varray

    def stringToNumber(self, cipheredText):
        _carray = []
        for i in cipheredText:
            _carray.append(ord(i) - 65)
        return _carray

    def numberToString(self, cipheredText):
        _carray = []
        for i in cipheredText:
            _carray.append(ord(i) + 65)
        return _carray

    def decipher(self):
        pass

    def splitText(self, cipheredText, length):
        return re.findall('.{1,length}', cipheredText)

    def frequencyOfLetters(self):
        _fol = [
            8.167, 1.492, 2.782, 4.253, 12.702, 2.228, 2.015, 6.094, 6.966,
            0.153, 0.772, 4.025, 2.406, 6.749, 7.507, 1.929, 0.095, 5.987,
            6.327, 9.056, 2.758, 0.978, 2.360, 0.150, 1.974, 0.074
        ]
        return _fol

    def ic(self, cipheredText, length):
        _possArray = []
        for i in self.splitText(cipheredText, length):
            _poss = 0
            for j in self.numberToString(i):
                _poss += pow(self.frequencyOfLetters()[j], 2)
            _possArray.append(_poss)
        return _possArray


def main():
    v = vigenere()
    print(v.ic('DLECYBRXNPKPYXVVOPXSDAICDAIC', 8))


if __name__ == '__main__':
    main()
