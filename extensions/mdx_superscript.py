"""Markdown Superscript Extension

Extend the Python-Markdown library to support superscript text with <sup> tags.

Usage
------

    Given the text:

        2^10^ is 1024.

    Output:

        2<sup>10</sup> is 1024.


Copyrights
------

Copyrights (c) 2018-2022 Li Yun <leven.cn@gmail.com>
"""

from markdown import Extension, Markdown
from markdown.inlinepatterns import SimpleTagPattern

# match ^, at least one character that is not ^, and ^ again
PATTERN = r"(\^)([^\^]+)\2"


class SuperscriptExtension(Extension):
    """Extension: text between ^ characters will be superscripted."""

    def extendMarkdown(self, md: Markdown):
        md.registerExtension(self)
        md.inlinePatterns.register(SimpleTagPattern(PATTERN, 'sup'), 'superscript', 9)


def makeExtension(*args, **kwargs):
    """Inform Markdown of the existence of the extension."""
    return SuperscriptExtension(*args, **kwargs)
