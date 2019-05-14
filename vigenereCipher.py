#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2019 miffyrcee <miffyrcee@localhost.localdomain>

# Distributed under terms of the MIT license.
"""
cipher
"""

import numpy


class vigenere(object):
    @classmethod
    def vigenereArray(self):
        s = shift('circle')
        _vigenereArray = numpy.zeros((26, 26), int)
        for i in range(0, 26):
            _vigenereArray[i] = s.shiftFunc(i)
        return _vigenereArray


class shift(object):
    def __init__(self, shiftType):
        self._shiftType = shiftType

    def shiftFunc(self, lenth):
        if (self._shiftType == 'circle'):
            return self.circleLine(lenth)

    def circleLine(self, lenth):
        def circleShiftLength(character, length):
            if (character + length > 90):
                return length - 26
            else:
                return length

        _uppercase = []
        for i in range(65, 91):
            _uppercase.append(i + circleShiftLength(i, lenth))
        return _uppercase


class vigenereCipher(object):
    #  def __init__(self, *args, **kwargs):
    #  for key, value in kwargs:
    #  cmd = 'self._%s = %s,(key,value)'
    #  exec(cmd)
    def __init__(self, plainKey, plainText, cipheredText):
        self._plainKey = plainKey
        self._plainText = plainText
        self._cipheredText = cipheredText

    def plainKeyToKey(self):
        keyGain = int(
            len(list(self._plainText)) / len(list(self._plainText))) + 1
        return keyGain * self._plainKey

    def toCipheredText(self):
        _vv = vigenere.vigenereArray()
        _key = self.plainKeyToKey()
        _j = 0
        for i in self._plainText:
            if (ord(i) == 32):
                self._cipheredText += ' '
            else:
                _j += 1
                self._cipheredText += chr(_vv[ord(_key[_j - 1]) - 65][ord(i) -
                                                                      65])
        return self._cipheredText

    @classmethod
    def toPlainText(self):
        finnalArray = ''
        _vv = vigenere.vigenereArray()
        for i in 'DLECYBRXNPKPYXVVOPXSDAICDAIC' [::8]:
            print(numpy.where(_vv == ord(i))[0])


def main():
    vp = vigenereCipher.toPlainText()
    print(vp)


if __name__ == '__main__':
    main()
