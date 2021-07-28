# column_print.py

A collection of small utilities to aid printing data
to a terminal window in columns.

## Utilities:

### ColumnPrinter

A context manager class to print successive print
statements in columns.

**Example Usage:**

```python
from modules.column_print import ColumnPrinter
with ColumnPrinter(2, 80) as cp:
    cp("Hello")
    cp("World")
```

Prints:

```
Hello                                   World
Goodbye                                 Moon
```

### print_list

A function to print a list of items in columns.

**Example usage:**

```python
from modules.column_print import ColumnPrinter
with ColumnPrinter(2, 80) as cp:
    cp.print_list(mylist)
```

## Supported Platforms:

* Linux (Windows and macOS to be added)
* Python 3.8 or Later


# Developing column_printer

To install column_printer, along with the tools you
need to develop and run tests, run the following in
your virtualenv:

```bash
$ pip install -e .[dev]
```

or, using pipenv:

```
$ pipenv install -e .
```

See also TODO.txt
