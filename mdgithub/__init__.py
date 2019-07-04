
from __future__ import absolute_import
from __future__ import unicode_literals

from markdown.extensions import Extension
from markdown.inlinepatterns import SimpleTagPattern, AutolinkInlineProcessor


STRIKE_RE = r'((?<!~)~~(?!~))(.*?)(?<!~)~~(?!~)'
AUTOMATIC_LINK_RE = '(https?://(?:[.,:)](?!\s)|[^\s.,:)])+)'


class GitHubExtension(Extension):
   def extendMarkdown(self, md, md_globals):
       # Strike-throw
       del_tag = SimpleTagPattern(STRIKE_RE, 'del')
       md.inlinePatterns.add('del', del_tag, '>not_strong')

       # Automatic links
       alink = AutolinkInlineProcessor(AUTOMATIC_LINK_RE, md)
       #md.inlinePatterns.register(alink, 'automatic_link', 65)
       md.inlinePatterns.add('automatic_link', alink, '>del')

       # Task Lists  TODO: implement

       # Tables -> use "table" extension, TODO: styling

       # Emoji, TODO: see https://github.com/ikatyang/emoji-cheat-sheet/blob/master/README.md


def makeExtension(*args, **kwargs):
    return GitHubExtension(*args, **kwargs)
