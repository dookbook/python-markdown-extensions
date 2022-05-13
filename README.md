## Welcome to Python Markdown Extensions

A collection of the [Python-Markdown](https://github.com/dookbook/python-markdown) library's extensions.

For more details see [Dookbook - Markdown Syntax](https://dookbook.info/content/62049b264d9f1a1af723760e/).

### Usage

```python
import markdown

md = markdown.markdown('text', extensions=['abbr'])
```

### Builtin Extensions

| Extension | Extension Name | Priority |
| --- | --- | --- |
| `AbbrExtension` | abbr | 16 |
| `AdmonitionExtension` | admonition | 105 |
| `AttrListExtension` | attr_list | 8 |
| `CodeHiliteExtension` | hilite | 30 |
| `DefListExtension` | defindent, deflist | 85, 25 |
| `FencedCodeExtension` | fenced_code_block | 25 |
| `FootnoteExtension` | footnote | 17 |
| `MetaExtension` | meta | 27 |
| `Nl2BrExtension` | nl | 5 |
| `TableExtension` | table | 75 |
| `TocExtension` | toc | 5 |
| `WikiLinkExtension` | wikilink | 75 |
| `SaneListExtension` | olist, ulist | 40, 30 |
| `MarkdownInHtmlExtension` | html_block, raw_html, markdown_block | 20, 30, 105 |
| `SmartyExtension` | smarty | 2 |

### Extensions

| Extension | Extension Name | Priority |
| --- | --- | --- |
| `DelInsExtension` | del, ins | 10, 11 |
| `SubscriptExtension` | sub | 9 |
| `SuperscriptExtension` | sup | 9 |
| `KeyboardInputExtension` | kbd | 9 |

### Syntax

#### `DelInsExtension`

```markdown
This is ++added content++ and this is ~~deleted content~~
```

#### `SubscriptExtension`

```markdown
The molecular composition of water is H~2~O.
```

#### `SuperscriptExtension`

```markdown
2^10^ is 1024.
```

For more details see [Dookbook - Markdown Syntax](https://dookbook.info/content/62049b264d9f1a1af723760e/).

### License

Under the BSD 3-Clause License.
