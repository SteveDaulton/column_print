#! /usr/bin/python3
# -*- coding: utf-8 -*-

"""Test ColumnPrinter class."""


from column_print import ColumnPrinter


print('***********************')
print('Three column')
print('60 char width')
print('Column separator = "| "')
print('***********************')


with ColumnPrinter(3,60, "| ") as cprint:
    cprint("Hello")
    cprint("World")
    cprint("Goodbye")
    cprint("Moon")
    cprint("Hello")
    cprint("World")
    cprint("Goodbye")
    cprint("Moon")
