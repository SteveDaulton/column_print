"""Utilities to print strings in columns.

ColumnPrinter:

Context manager class:
Prints in columns

Example:

  from modules.column_print import ColumnPrinter
  with ColumnPrinter() as cp:
      cp("Hello")
      cp("World")

Prints:

Hello                                   World
Goodbye                                 Moon

"""

class ColumnPrinter:
    """..."""
    def __init__(self, columns=2, width=80):
        self.columns = columns
        self.width = width
        self.col_count = 0
        self.col_width = self.width // self.columns

    def __enter__(self):
        return self

    def __call__(self, txt):
        """Print in columns."""
        col_required = 1 + (len(txt) // self.col_width)
        col_remain = self.columns - self.col_count
        # If can't fit on line, start new line.
        if col_required > col_remain:
            print('')
            self.col_count = 0
        # If not filling line, calculate padding.
        if self.col_count + col_required < self.columns:
            pad = min(self.width, self.col_width * col_required)
        else:
            pad = 0
        print('{:<{width}s}'.format(txt, width=pad), end='')
        # Increment column count.
        if self.col_count >= self.columns:
            self.col_count = col_required
        else:
            self.col_count +=  col_required

    def __exit__(self, exc_type, exc_value, exc_traceback):
        print('')
