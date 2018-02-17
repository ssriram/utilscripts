#!/usr/bin/env python

import requests
import urllib
import lxml.html

GOOGLE_BASE='http://google.com/search?q='

def search_for(s):
    page_text = requests.get(GOOGLE_BASE + urllib.quote(s)).text
    parsed = lxml.html.fromstring(page_text)
    urls = [link.str for link in parsed.cssselect('cite')]
    return urls

if __name__ == '__main__':
    print search_for('site:.in')
