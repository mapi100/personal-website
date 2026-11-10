#!/usr/bin/env python3
"""Dependency-free portfolio checks. Run: python3 tools/check_site.py."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
PAGES = ('index.html', 'about.html', 'projects.html', 'seminary-portal.html')

class Page(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.ids, self.links, self.meta, self.images = [], [], {}, []
        self.titles = self.h1s = self.mains = 0
        self.lang = None
        self.canonical = None
    def handle_starttag(self, tag, attributes):
        a = dict(attributes)
        if 'id' in a:
            self.ids.append(a['id'])
        if tag == 'html': self.lang = a.get('lang')
        if tag == 'title': self.titles += 1
        if tag == 'h1': self.h1s += 1
        if tag == 'main': self.mains += 1
        if tag == 'meta': self.meta[a.get('name') or a.get('property')] = a.get('content')
        if tag == 'link' and a.get('rel') == 'canonical': self.canonical = a.get('href')
        if tag == 'img': self.images.append(a)
        for key in ('href', 'src'):
            if a.get(key): self.links.append(a[key])

pages = {}
for filename in PAGES:
    page = Page()
    page.feed((ROOT / filename).read_text(encoding='utf-8'))
    assert page.lang == 'en', (filename, 'English page language missing')
    assert page.titles == page.h1s == page.mains == 1, (filename, 'Expected one title, h1, and main')
    assert len(page.ids) == len(set(page.ids)), (filename, 'Duplicate IDs')
    assert 'main' in page.ids, (filename, 'Skip-link target missing')
    assert page.canonical and page.canonical.startswith('https://marcopenaibarra.com/'), filename
    for field in ('description', 'og:title', 'og:description', 'og:image', 'og:image:alt', 'og:url', 'twitter:card'):
        assert page.meta.get(field), (filename, field)
    for image in page.images:
        assert image.get('alt') and image.get('width') and image.get('height'), (filename, image)
    pages[filename] = page

checks = 0
for filename, page in pages.items():
    for link in page.links:
        url = urlsplit(link)
        if url.scheme or url.netloc: continue
        target = (ROOT / unquote(url.path)) if url.path else ROOT / filename
        assert target.is_file(), (filename, 'Missing file', link)
        if url.fragment:
            assert target.name in pages and unquote(url.fragment) in pages[target.name].ids, (filename, 'Missing fragment', link)
        checks += 1
    print('PASS', filename, 'structure, metadata, image attributes, local links and fragments')
for path in (ROOT / 'documents').glob('*.pdf'):
    assert path.read_bytes().startswith(b'%PDF-'), path.name
    checks += 1
sitemap = ET.parse(ROOT / 'sitemap.xml')
urls = [node.text for node in sitemap.findall('.//{http://www.sitemaps.org/schemas/sitemap/0.9}loc')]
assert urls == ['https://marcopenaibarra.com/', 'https://marcopenaibarra.com/about.html', 'https://marcopenaibarra.com/projects.html', 'https://marcopenaibarra.com/seminary-portal.html'], urls
print(f'PASS {checks} local references/PDF checks; sitemap includes all four pages')
print('External destination reachability requires a separate network check.')
