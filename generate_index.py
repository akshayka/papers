import collections
import glob
import re
import pdb

MD_WILDCARD = 'summaries/*.md'
HTML_WILDCARD = 'html/*.html'
TITLE_PATTERN = r'^# \[(.*?) \(([a-zA-z]*) ([0-9]{4})\)'

md_files = sorted(glob.glob(MD_WILDCARD))
html_files = sorted(glob.glob(HTML_WILDCARD))

ListItem = collections.namedtuple('ListItem', ['title', 'author', 'year', 'url'])
list_items = []

for md_file, html_file in zip(md_files, html_files):
    with open(md_file, 'rb') as f:
        title_line = f.readline()
        match = re.search(TITLE_PATTERN, title_line)
        title = match.group(1)
        author = match.group(2)
        year = int(match.group(3))
        url = html_file
        list_items.append(ListItem(title, author, year, url))

list_items = sorted(list_items, key=lambda t: t.year)

print '<ol>'
for list_item in list_items:
    print '<li><a href="%s">%s <span class="year">(%s %d)</span></a></li>' % (
        list_item.url, list_item.title, list_item.author, list_item.year)
print '</ol>'

