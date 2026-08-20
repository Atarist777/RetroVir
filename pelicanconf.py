#!/usr/bin/env python
# -*- coding: utf-8 -*-

AUTHOR = 'Draedon'
SITENAME = 'Retrovir'
SITESUBTITLE = 'Retro Computing'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Moscow'
DEFAULT_LANG = 'en'

THEME = 'themes/mytheme'
STATIC_PATHS = ['gallery']

ARTICLE_PATHS = ['articles']
PAGE_PATHS = ['pages']

CATEGORY_URL = '{slug}/'
CATEGORY_SAVE_AS = '{slug}/index.html'

TAGS_SAVE_AS = 'tags.html'
TAG_SAVE_AS = 'tag/{slug}.html'
TAG_URL = 'tag/{slug}.html'

DEFAULT_PAGINATION = 6

ARTICLE_ORDER_BY = 'title'

DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False

AUTHORS_SAVE_AS = ''
CATEGORIES_SAVE_AS = ''

RELATIVE_URLS = True

PLUGIN_PATHS = ['plugins']
PLUGINS = ['json_search']

FEED_ALL_ATOM = None
FEED_ALL_RSS = None