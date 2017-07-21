import collections
import glob
import re
import pdb

META_EXT= '.meta'
SUM_WILDCARD = 'summaries/*'
HTML_WILDCARD = 'html/*.html'
TITLE_PATTERN = r'^# \[(.*?) \(([a-zA-z\']*) ([0-9]{4})\)'

sum_files = sorted(glob.glob(SUM_WILDCARD))
html_files = sorted(glob.glob(HTML_WILDCARD))

ListItem = collections.namedtuple('ListItem', ['title', 'author', 'year', 'url'])
list_items = []

for sum_file, html_file in zip(sum_files, html_files):
    with open(sum_file, 'rb') as f:
        title_line = f.readline()
        match = re.search(TITLE_PATTERN, title_line)
        title = match.group(1)
        author = match.group(2)
        year = int(match.group(3))
        if sum_file.endswith(META_EXT):
            basename = sum_file.split('summaries/')[1]
            url = 'pdf/' + basename.split(META_EXT)[0] + '.pdf'
        else:
            url = html_file
        list_items.append(ListItem(title, author, year, url))

list_items = sorted(list_items, key=lambda t: t.year)

print '<ol>'
for list_item in list_items:
    print '<li><a href="%s">%s <span class="year">(%s %d)</span></a></li>' % (
        list_item.url, list_item.title, list_item.author, list_item.year)
print '</ol>'
