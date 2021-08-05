#! /usr/bin/python3
# -*- coding: utf-8 -*-

"""Test ColumnPrinter class with default settings."""


from column_print import ColumnPrinter


print('****************')
print('Two column test:')
print('(default layout)')
print('****************')

with ColumnPrinter() as cp:
    cp("Hello")
    cp("World")
    cp("Goodbye")
    cp("Moon")
    cp("Now is the time for all good men")
    cp("to come to the aid of the party.")
    cp("Goodbye")
    cp("The quick brown fox jumped over the lazy dog.")
    cp("Moon")
    cp("Hello")
    cp("World")
    cp("Goodbye")
    cp("Moon")
