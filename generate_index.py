import collections
import glob
import re

PDF_META = 'PDF'
MD_WILDCARD = 'summaries/*.md'
HTML_WILDCARD = 'html/*.html'
TITLE_PATTERN = r'^# \[(.*?) \(([a-zA-z\s\']*) ([0-9]{4})\)'

md_files = sorted(glob.glob(MD_WILDCARD))
html_files = sorted(glob.glob(HTML_WILDCARD))
assert(len(md_files) == len(html_files))

ListItem = collections.namedtuple(
  'ListItem', ['title', 'author', 'year', 'url'])
list_items = []

for md_file, html_file in zip(md_files, html_files):
    with open(md_file, 'r') as f:
        title_line = f.readline()
        match = re.search(TITLE_PATTERN, title_line)
        title = match.group(1)
        author = match.group(2)
        year = int(match.group(3))
        meta = f.readline().strip()
        if meta == PDF_META:
            basename = md_file.split('summaries/')[1]
            url = 'pdf/' + basename.split('.md')[0] + '.pdf'
        else:
            url = html_file
        list_items.append(ListItem(title, author, year, url))

list_items = sorted(list_items, key=lambda t: t.year)

print('<ol>')
for list_item in list_items:
    print('<li><a href="%s">%s <span class="year">(%s %d)</span></a></li>' % (
        list_item.url, list_item.title, list_item.author, list_item.year))
print('</ol>')
