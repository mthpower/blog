#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

import os

AUTHOR = u'Matthew Power'
SITENAME = u'Matthew'
SITESUBTITLE = u'Python and other experiments'
SITEURL = 'http://localhost:8000'

PATH = 'content'

TIMEZONE = 'Europe/London'

DEFAULT_LANG = u'en'

RELATIVE_URLS = False

# Pretty URLs
ARTICLE_URL = 'article/{slug}'
ARTICLE_SAVE_AS = 'article/{slug}/index.html'
PAGE_URL = 'page/{slug}'
PAGE_SAVE_AS = 'page/{slug}/index.html'
CATEGORY_URL = 'category/{slug}'
CATEGORY_SAVE_AS = 'category/{slug}/index.html'
TAG_URL = 'tag/{slug}'
TAG_SAVE_AS = 'tag/{slug}/index.html'
ARCHIVES_SAVE_AS = 'archives/index.html'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

# Theme
THEME = os.path.join(os.path.dirname(__file__), 'theme/blue-penguin')

# Static
STATIC_PATHS = ['img']
