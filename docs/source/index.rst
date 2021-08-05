column_print
============

This module provides a simple way to print multiple short strings to a terminal
in columns.

Unlike many similar utilities, it is not necessary for the strings to be in a
list before printing, though 'print_list' is also provided for printing lists.

**ColumnPrinter:** A context manager class, can print any sequence of strings
without knowing the length or number of strings in advance.

**print_list:** A function, prints a list to the terminal in equally spaced
columns.

Note that this module is NOT intended for printing tables, but simply to
display a long list more conveniently. For printing tables,
`tabulate <https://pypi.org/project/tabulate/>`_ or
`columnize <https://pypi.org/project/columnize/>`_ may be more suitable.

.. toctree::

   module
   class
   print-list
   examples
   examples2
