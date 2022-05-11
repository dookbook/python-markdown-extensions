"""Markdown Subscript Extension

Extend the Python-Markdown library to support subscript text with <sub> tags.

Usage
------

    Given the text:

        The molecular composition of water is H~2~O.

    Output:

        <p>The molecular composition of water is H<sub>2</sub>O.</p>


Copyrights
------

Copyrights (c) 2018-2022 Li Yun <leven.cn@gmail.com>
"""

from markdown import Extension, Markdown
from markdown.inlinepatterns import SimpleTagPattern

# match ~, at least one character that is not ~, and ~ again
PATTERN = r"(\~)([^\~]+)\2"


class SubscriptExtension(Extension):
    """Extension: text between ~ characters will be subscripted."""

    def extendMarkdown(self, md: Markdown):
        """Insert 'subscript' pattern before 'not_strong' pattern."""
        md.registerExtension(self)
        md.inlinePatterns.register(SimpleTagPattern(PATTERN, 'sub'), 'subscript', 9)


def makeExtension(*args, **kwargs):
    """Inform Markdown of the existence of the extension."""
    return SubscriptExtension(*args, **kwargs)
