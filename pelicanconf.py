#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Zachary Priddy'
SITENAME = 'zpriddy.com'
SITEURL = 'https://www.zpriddy.com'

THEME = "./pure-single"

PATH = 'content'

TIMEZONE = 'US/Pacific'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Github', 'https://github.com/zpriddy'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

MENUITEMS = (
    ('HOME','https://zpriddy.com/'),
    ('PROJECTS','https://zpriddy.com/category/projects/'),
    ('FIREFLY HOME','https://Firefly-Home.io'),
    ('ABOUT','https://zpriddy.com/pages/about-me'),
    )

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True