#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'CS Minds'
SITENAME = u'CS Minds'
SITEURL = ''
LOAD_CONTENT_CACHE = False
PATH = 'content'
OUTPUT_PATH = '../output/'

TIMEZONE = 'Europe/Dublin'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
JINJA_ENVIRONMENT = {
    'extensions': ['jinja2.ext.i18n', 'jinja2.ext.do'],
}
PLUGIN_PATHS = ['plugins/', ]
PLUGINS = ['i18n_subsites',
           'liquid_tags.youtube',
           'series',
           ]

MARKUP = ('md',)
ARTICLE_PATHS = ['articles']
STATIC_PATHS = ['img', 'pdf']
PAGE_PATHS = ['pages']
THEME = 'theme'
ARTICLE_URL = 'articles/{slug}.html'
ARTICLE_SAVE_AS = 'articles/{slug}.html'
# TEMPLATE_PAGES = {'listSeries.json': 'api/listSeries.json', }
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'

ARTICLE_ORDER_BY = 'sortorder'
SUMMARY_MAX_LENGTH = 20
# Blogroll
# LINKS = (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),
#          ('You can modify those links in your config file', '#'),)
#
# # Social widget
# SOCIAL = (('You can add links in your config file', '#'),
#           ('Another social link', '#'),)

DEFAULT_PAGINATION = False
MENUITEMS = [
    {
        'title': 'About',
        'link': '/about.html',
    },
    {
        'title': 'Events',
        'link': '/events.html',
    },
    {
        'title': 'Activities',
        'link': '/activities.html',
    },
    {
        'title': 'CS Myths',
        'link': '/cs-myths.html',
    },
    {
        'title': 'Women in STEM',
        'link': '/women-in-cs.html',
    },
    {
        'title': 'Contact Us',
        'link': '/contact-us.html',
    },
]

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
MODELLING_DESC = "3D Modelling allows for a huge amount of creativity and imagination without having to learn any code. Find out how to make an ice cream and play a game of bowling in Blender. Once you have these mastered, try some of the advanced projects."
MUSIC_DESC = "Learn to make music using SoundTrap, a website, and record and edit your voice and mix it with your music in Audacity, a free audio tool. You can record and edit your own songs, or add some well know songs and make them your own."
WEBANDVR_DESC = "Create your own reality without having to install anything. Learn how to make a treasure hunt on Gltich, a website, using the AFrame framework. Where you hunt for and what you are looking for is totally up to you."
SETANTA_DESC = "Setanta is an new all-Irish programming language. Find out how to use Setanta to make animations, games and more, and learn some Irish along the way. Setanta is suitable for everyone, from total beginners to programming experts. Setanta runs in your browser, so there's no need to install anything! "
CATEGORY_MAP = {
    '3D Modelling': MODELLING_DESC,
    'Music Technology': MUSIC_DESC,
    'Web & VR': WEBANDVR_DESC,
    'Setanta': SETANTA_DESC,
}
