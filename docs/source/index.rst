column_print
============

This module provides :ref:`ColumnPrinter`, and :ref:`print_list`.

**ColumnPrinter:** A context manager class, can print any sequence of strings
without knowing the length or number of strings in advance.

**print_list:** A function, prints a list to the terminal in equally spaced
columns.

.. note::

   This module is NOT intended for printing tables, but simply to display long
   lists more conveniently. For printing tables, `tabulate <https://pypi.org/project/tabulate/>`_ or
   `columnize <https://pypi.org/project/columnize/>`_ may be more suitable.


Module: column_print
====================

.. automodule:: column_print


Usage::

   with ColumnPrinter(columns=int, width=int, colsep=str) as VAR:
       VAR(<printable-expression>)


Examples
--------
See :ref:`ColumnPrinter-examples`

=========

.. _ColumnPrinter:

Class: ColumnPrinter
====================

.. autoclass:: column_print::ColumnPrinter
   :members:

==========

.. _print_list:

Function: print_list
====================

.. autofunction:: column_print.print_list


Usage::

   column_print.print_list(list-of-printables, width=int, colsep=str)


Examples
--------
See :ref:`print_list-examples`

=============

.. toctree::

   examples
   examples2
