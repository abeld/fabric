"""
.. versionadded:: 0.9.2

Functions for wrapping strings in ANSI color codes.

Each function within this module returns the input string ``text``, wrapped
with ANSI color codes for the appropriate color.

For example, to print some text as green on supporting terminals::

    from fabric.colors import green

    print(green("This text is green!"))

Because these functions simply return modified strings, you can nest them::

    from fabric.colors import red, green

    print(red("This sentence is red, except for " + green("these words, which are green") + "."))

If ``bold`` is set to ``True``, the ANSI flag for bolding will be flipped on
for that particular invocation, which usually shows up as a bold or brighter
version of the original color on most terminals.
"""


__all__ = [
    'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white',
    'bold_red', 'bold_green', 'bold_yellow', 'bold_blue', 'bold_magenta',
    'bold_cyan', 'bold_white'
    ]


def _wrap_with(code):
    def inner(text, bold=False):
        c = code
        if bold:
            c = "1;%s" % c
        return "\033[%sm%s\033[0m" % (c, text)
    return inner

def _bold_wrap_with(code):
    def inner(text):
        return "\033[1;%sm%s\033[0m" % (code, text)
    return inner


red = _wrap_with('31')
green = _wrap_with('32')
yellow = _wrap_with('33')
blue = _wrap_with('34')
magenta = _wrap_with('35')
cyan = _wrap_with('36')
white = _wrap_with('37')


bold_red = _bold_wrap_with('31')
bold_green = _bold_wrap_with('32')
bold_yellow = _bold_wrap_with('33')
bold_blue = _bold_wrap_with('34')
bold_magenta = _bold_wrap_with('35')
bold_cyan = _bold_wrap_with('36')
bold_white = _bold_wrap_with('37')
