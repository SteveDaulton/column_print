.. _ColumnPrinter-examples:

ColumnPrinter Examples
======================

1. **Initialise ColumnPrinter with no arguments**::

    from column_print import ColumnPrinter

    with ColumnPrinter() as cprint:
        cprint("Hello")
        cprint("World")
        cprint("Goodbye")
        cprint("Moon")

Prints::

    Hello                                    World
    Goodbye                                  Moon


2. **Initialise ColumnPrinter with keyword arguments**::

    from column_print import ColumnPrinter

    with ColumnPrinter(columns=3, width=60) as cprint:
        cprint("Hello")
        cprint("World")
        cprint("Goodbye")
        cprint("Moon")

Prints::

    Hello               World               Goodbye
    Moon


3. **Print an unknown number of strings of unknown length**::

    from string import ascii_letters
    from secrets import choice
    from random import randint

    from column_print import ColumnPrinter

    with ColumnPrinter(columns=3, width=70) as cprint:
        for i in range(randint(10, 20)):
            length = randint(1, 20)
            cprint(''.join(choice(ascii_letters) for _ in range(length)))

Prints::

    KPTyqazKuwoY           dGYCzBIAkju            aXQtXhw
    JvnTfKkzabb            mcjZvqvXLdG            IadYqxaZ
    cHm                    dReYhbhNkhEw           HaVaEkdjQNGHUIlywzjK
    PCHXF
