#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2019 miffyrcee <miffyrcee@localhost.localdomain>
# Distributed under terms of the MIT license.
"""

"""
import itertools
import re
import string
import time


import matplotlib.pyplot as plt
import numpy as np
from pycipher import Vigenere



import pycipher
class vigenere(object):
    @property
    def vigenerearray(self):
        _varray = np.zeros((26, 26), int)
        for i in range(0, 26):
            for j in range(0, 26):
                _varray[i][j] = (i + j) % 26
        return _varray

    def decipher(self, cipheredText):
        print(pycipher.Caesar(key=8).decipher(cipheredText))

    def length(self, cipheredText):
        _chararr = {}
        _cipher = [cipheredText[i:i + 3] for i in range(len(cipheredText) - 2)]
        for i in _cipher:
            for j in np.where(np.array(_cipher) == i):
                _chararr[len(j)] = j

        _post = _chararr[np.max(list(_chararr.keys()))]
        _postarr = [_post[i + 1] - _post[0] for i in range(len(_post) - 1)]
        return np.gcd.reduce(_postarr)

    def mic(self, cipheredText):
        _textarr = np.array_split(list(cipheredText), 7)
        _post = [(0, i) for i in range(1, 7)]
        for i, j in _post:
            _possa = []
            for k in string.ascii_lowercase:
                for l in np.where(_textarr[i] == k):
                    _possa.append(len(l) / len(_textarr[i]))
            _possb = []
            for k in string.ascii_lowercase:
                for l in np.where(_textarr[j] == k):
                    _possb.append(len(l) / len(_textarr[j]))
            print(np.array(_possa) * np.array(_possb))

    def _POL(self):
        _fol = [
            8.167, 1.492, 2.782, 4.253, 12.702, 2.228, 2.015, 6.094, 6.966,
            0.153, 0.772, 4.025, 2.406, 6.749, 7.507, 1.929, 0.095, 5.987,
            6.327, 9.056, 2.758, 0.978, 2.360, 0.150, 1.974, 0.074
        ]
        return _fol

    def ic(self, cipheredText):
        _possArray = {}
        for j in range(1, 11):
            _poss = []
            for i in np.array_split(np.array(list(cipheredText)), j):
                _poss.append(self.singleIc(''.join(i)))
            _possArray[j] = _poss
        return _possArray

    def singleIc(self, cipheredText):
        _poss = 0
        for i in np.unique(list(cipheredText)):
            for j in np.where(np.array(list(cipheredText)) == i):
                _poss += pow(len(j) / len(cipheredText), 2)
        return _poss


def main():
    strings = 'ahmnywiwoeeraltllbisqxvrgusewhsbahbskoermbmvhubknfeibhgvzhvrosrfmoelchsudubkfgyrlvozsiohgoydfohzifloairghxmeerrvfoaivbtfvnrjgsjvmhfanqoenisayyaaghusatuvgywatrefrsjhrfmbmkoabhjjptrgczwahvfkbmsdpbacjvmvfsndsoshgnfkaobjrsslqbbblyeghfamudreoaqjiepizkaaapsfaaifxbboutunhvldaflchooourzcwkufgctwaajnmsjvmurfrsudnyzjgblqosygztvsmbmzhbhzqkoojlchjzeyskrsyethoevldqnmnfknvtvgakoabhpsyelbinjlnbgvrjldbacgtltebiodldbaalsjcbhbgfvtuvbtoplyuochlngbarloeanhvguayngfwtbyrkvdssubkywuiraqlxhrrjsydahrzcflsoirrbxteaosdmpegvtlgbcnahnclcnesbxfohegrdmfbealkllsvqnfuogjfvllaalabjlbhgbbloiatwaloejbfyvjohyrflvpzrhbskoermbmbpgbhuwkengv'
    v = vigenere()
    results = 'iamaliveheremybelovedforthereasontoadoreyouohhowanxiousihavebeenforyouandhowsorryiamaboutallyoumusthavesufferedinhavingnonewsfromusmayheavengrantthatthisletterreachesyoudonotwritetomethiswouldcompromiseallofusandabovealldonotreturnunderanycircumstancesitisknownthatitwasyouwhohelpedustogetawayfromhereandallwouldbelostifyoushouldshowyourselfweareguardeddayandnightidonotcareyouarenotheredonotbetroubledonmyaccountnothingwillhappentomethenationalassemblewillshowleniencyfarewellthemostlovedofmenbequietifyoucantakecareofyourselfformyselficannotwriteanymorebutnothingintheworldcouldstopmetoadoreyouuptothedeath'
    #  print(v.ic(strings))
    print(v.length('DLECYBRXNPKPYXVVOPXSDAICDAIC'))
    print(v.mic(strings))


    print(np.sum([i * i for i in v._POL()]))



if __name__ == '__main__':
    main()
