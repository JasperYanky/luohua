#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 落花 / 测试套件 / 认证 / 包
#
# Copyright (C) 2013 JNRain
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from __future__ import unicode_literals, division

from luohua.auth.user import User


TEST_USERS = {
        '9fabe73980ff48aba62303812aa93765': {
            '_V': 1,
            'a': 'test0',
            'e': 'test0@example.com',
            'p': (
                'lh1$ZcMloWnpTCDoCwXI|f9b2fcb14e85afd8333cc969275f27ab1343e7'
                '8a414c9c7f52507d5e53436df62f8f16f55fb383a1a9a88971b3f152566'
                '0e6ff6b6f49c2a9f1c7b9f58adce29c'
                ),
            'r': [],
            },
        '0012cdf931a64c01ab97cb26f5f84bf0': {
            '_V': 1,
            'a': 'test2',
            'e': 'fsck+qq@youknow.com',
            'p': 'kbs$0b84f4bb2b3c572572015dd1050b3232',
            'r': [],
            },
        }
TEST_PASSWORDS = {
        '9fabe73980ff48aba62303812aa93765': 'testtest',
        '0012cdf931a64c01ab97cb26f5f84bf0': 'woshiruomima',
        }


def setup_package():
    # 设置几个测试用户, 权限之类的数据
    with User.storage as conn:
        for uid, data in TEST_USERS.iteritems():
            conn.new(uid, data).store()
            print '[+User] %s' % uid


def teardown_package():
    # 把测试数据扔掉
    with User.storage as conn:
        for uid in TEST_USERS:
            conn.get(uid).delete()
            print '[-User] %s' % uid


# vim:set ai et ts=4 sw=4 sts=4 fenc=utf-8:
