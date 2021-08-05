.. _print_list-examples:

print_list Examples
===================

1. **With 'pipe' column separator**::

    from column_print import print_list

    data = ['Hello',
            'World',
            123,
            42,
            'foobar',
            '127.0.0.1',
            'Home Sweet Home']

    print_list(data, colsep='|')


Prints::

    Hello           |World           |123             |42              |foobar
    127.0.0.1       |Home Sweet Home                  |

