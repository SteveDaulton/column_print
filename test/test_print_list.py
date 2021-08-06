#! /usr/bin/python3
# -*- coding: utf-8 -*-

"""Test 'print_list' with default settings."""


from column_print import print_list

data = ['Hello',
        'World',
        123,
        42,
        'foobar',
        '127.0.0.1',
        'Home Sweet Home']

print_list(data, colsep='|')
