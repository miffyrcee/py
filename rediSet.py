#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2019 miffyrcee <miffyrcee@localhost.localdomain>
#
# Distributed under terms of the MIT license.
"""

"""
import json

import redis

pool = redis.ConnectionPool(host='149.129.115.88',
                            port=6379,
                            db=0,
                            password='foobared')

r = redis.Redis(connection_pool=pool)
r.set('test', 1)
r.append('test', 2)
print(r.get('test'))
print(12 > float(r.get('temperature')))
if float(234) > float(r.get('concentration')):
    print("sdf")
