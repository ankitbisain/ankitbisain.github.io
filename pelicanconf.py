import os
import markdown.util

AUTHOR = 'Ankit Bisain'
SITENAME = 'ankit bisain'
SITESUBTITLE=u'ankitb12 [at] mit [dot] edu'
BLOG_TITLE=u'brian lee'
BLOG_SUBTITLE=u'ankit\'s blog'
PATH = 'content'
TIMEZONE = 'America/New_York'
DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
GITHUB_URL = 'https://github.com/ankitbisain/ankitbisain.github.io'

# Article settings
ARTICLE_PATHS= ['posts']
ARTICLE_URL = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'
DEFAULT_METADATA = {'status': 'draft'}

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

#PLUGINS = ['pelican.plugins.render_math']
PLUGIN_PATHS=['plugins']
PLUGINS = ['pelican_katex']

for tag in ('figure', 'figcaption'):
    markdown.util.BLOCK_LEVEL_ELEMENTS.remove(tag)

DISPLAY_PAGES_ON_MENU = True

#page
PAGE_PATHS=['pages']
PAGE_URL='{slug}'
PAGE_SAVE_AS = '{slug}.html'

#THEME SETTINGS
THEME = './theme/'

ABOUT_PAGE = '/pages/about.md'
GITHUB_USERNAME = 'ankitbisain'

ENABLE_MATHJAX = False
MATH_JAX = {
    "auto_insert": False,
    "process_summary": False,
} 



# Footer info
LICENSE_URL = 'https://github.com/brianjsl/brianjsl.com/blob/main/LICENSE'
LICENSE = "MIT"

# templates

DIRECT_TEMPLATES= ['index']

DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False

#static
STATIC_PATHS=['images', 'files', 'favicon.ico']

EXTRA_PATH_METADATA = {
    'extra/favicon.ico': {'path': 'favicon.ico'},  # and this
    'extra/CNAME': {'path': 'CNAME'},
    'extra/LICENSE': {'path': 'LICENSE'},
    'extra/README': {'path': 'README'},
}
