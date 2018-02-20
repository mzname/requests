# -*- coding: utf-8 -*-

"""
requests.compat
~~~~~~~~~~~~~~~

This module handles import compatibility issues between Python 2 and
Python 3.
"""

import chardet

import sys

# -------
# Pythons
# -------

#: Python 3.x?
is_py3 = (sys.version_info[0] == 3)

# ---------
# Specifics
# ---------

# from urllib.parse import urlparse, urlunparse, urljoin, urlsplit, urlencode, quote, unquote, quote_plus, unquote_plus, urldefrag
# from urllib.request import parse_http_list, getproxies, proxy_bypass, proxy_bypass_environment, getproxies_environment
# from http import cookiejar as cookielib
# from http.cookies import Morsel
# from io import StringIO


basestring = (str, bytes)
numeric_types = (int, float)
integer_types = (int,)
