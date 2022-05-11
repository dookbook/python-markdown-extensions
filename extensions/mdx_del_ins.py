"""Markdown Deletion/Insertion Extension

Extend the Python-Markdown library to wrap the inline content with <del>/<ins> tags.

Usage
------

    Given the text:

        This is ++added content++ and this is ~~deleted content~~.

    Output:

        <p>This is <ins>added content</ins> and this is <del>deleted content</del>.</p>


Copyrights
------

Copyrights (c) 2011-2012 [The active archives contributors](http://activearchives.org/)
Copyrights (c) 2020-2022 Li Yun <leven.cn@gmail.com>
"""


from markdown import Markdown
from markdown.extensions import Extension
from markdown.inlinepatterns import SimpleTagPattern


DEL_PATTERN = r"(\~\~)(.+?)(\~\~)"
INS_PATTERN = r"(\+\+)(.+?)(\+\+)"


class DelInsExtension(Extension):
    """Adds DelIns extension."""

    def extendMarkdown(self, md: Markdown):
        """Insert del and ins patterns before 'not_strong' pattern."""
        md.registerExtension(self)
        md.inlinePatterns.register(SimpleTagPattern(DEL_PATTERN, 'del'), 'del', 10)
        md.inlinePatterns.register(SimpleTagPattern(INS_PATTERN, 'ins'), 'ins', 11)


def makeExtension(*args, **kwargs):
    """Inform Markdown of the existence of the extension."""
    return DelInsExtension(*args, **kwargs)
