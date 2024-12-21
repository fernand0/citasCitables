#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'Fernando Tricas García'
SITENAME = 'Citas Citables'
SITEURL = 'https://citascitables.elmundoesimperfecto.com/'

PATH = 'content'

TIMEZONE = 'Europe/Madrid'

DEFAULT_LANG = 'es'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feed'
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
         ('El Mundo es Imperfecto', 'https://elmundoesimperfecto.com/')
         )

# Social widget
SOCIAL = (('Twitter', 'https://twitter.com/fernand0'),
          ('Mastodon', 'https://mastodon.social/@fernand0'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
