#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Svend Vanderveken'
SITENAME = u"Svend Vanderveken"
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Brussels'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = ()

# Social widget (any font name from http://fontawesome.io/icons/ should work here)
SOCIAL = (
         ("github", 'https://github.com/sv3nd'),
     	 ("twitter", 'https://twitter.com/svend_x4f'),
     	 ("linkedin", 'https://be.linkedin.com/in/vanderveken'),
     	 ("stack-overflow", 'http://stackoverflow.com/users/3318335/svend'),
         )

GOOGLE_ANALYTICS = 'UA-101598127-1'

SUMMARY_MAX_LENGTH = 50

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = '/Users/svend/dev/perso/pelican_themes/pelican-hyde'

MARKUP = ('md', 'ipynb')

PLUGIN_PATHS = ['./plugins']
PLUGINS = [ 'ipynb.markup']

IGNORE_FILES = [".ipynb_checkpoints"]

BIO = "I am a freelance Data Engineer, I focus on scalable data processing pipelines based on Spark, Kafka, Cassandra... I love to code, preferably in Scala, Python and SQL."
PROFILE_IMAGE = "blog/svend.jpg"
