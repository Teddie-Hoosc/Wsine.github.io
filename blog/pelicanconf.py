#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Wsine'
SITENAME = "Wsine's Blog"
SITESUBTITLE = "To be simple, to be powerful."
SITEURL = 'http://Wsine.github.io/blog'
# SITEURL = '.'
PROFILE_IMAGE_URL = 'http://Wsine.github.io/blog/content/img/personImg.jpg'

# Set the source files
PATH = 'content'
ARTICLE_PATHS = ['blog']
ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}.html'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}.html'
STATIC_PATHS = ['misc', 'img']
MENUITEMS = [('blog', '/blog/output'), ('cv', '/blog/content/misc/cv.pdf')]

# Set the area
TIMEZONE = 'America/Chicago'

# Set Language
DEFAULT_LANG = 'en'
# Set Date
DATE_FORMATS = {
    'en': ('usa','%a, %d %b %Y'),
    'jp': ('jpn','%Y-%m-%d(%a)'),
}

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# feed
FEED_RSS = '/blog/output/feeds/rss.xml'
FEED_MAX_ITEMS = 10

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 3

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# Add Theme
THEME = "crowsfoot"
# THEME = "notmyidea"

# Address
EMAIL_ADDRESS = 'weizhy3@hotmail.com'
GITHUB_ADDRESS = 'http://github.com/Wsine'
# SO_ADDRESS = 'http://stackoverflow.com/users/1663558/james-porter'
# TWITTER_ADDRESS = 'http://twitter.com/porterjamesj'

# License
LICENSE_NAME = "none"
LICENSE_URL = "#"