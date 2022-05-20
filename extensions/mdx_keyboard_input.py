"""Markdown Keyboard Input Extension

Extend the Python-Markdown library to support keyboard input text with <kbd> tags.

Usage
------

    Given the text:

        !!!Ctrl!!! + !!!C!!!

    Output:

        <kbd>Ctrl</kbd> + <kbd>C</kbd>


Copyrights
------

Copyrights (c) 2018-2022 Li Yun <leven.cn@gmail.com>
"""

from markdown import Extension, Markdown
from markdown.inlinepatterns import InlineProcessor
from markdown.util import etree

# match !!!, at least one character that is not !, and !!! again
PATTERN = r'!{3}([^!]+)!{3}'


class KeyboardInputPattern(InlineProcessor):
    def handleMatch(self, m, data):
        elem = etree.Element('kbd')
        elem.text = m.group(1)
        return elem, m.start(0), m.end(0)


class KeyboardInputExtension(Extension):
    """Extension: text between !!! characters will be rendered as keyboard input."""

    def extendMarkdown(self, md: Markdown):
        md.registerExtension(self)
        md.inlinePatterns.register(KeyboardInputPattern(PATTERN), 'kbd', 9)


def makeExtension(*args, **kwargs):
    """Inform Markdown of the existence of the extension."""
    return KeyboardInputExtension(*args, **kwargs)
