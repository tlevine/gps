#!/usr/bin/env python
# http://en.nederlandfietsland.nl/en/long-distance-cycle-routes/gps-tracks
import sys, os

import lxml.html, requests

wiki_url = 'http://wiki.openstreetmap.org/wiki/WikiProject_Europe/EuroVelo'
gpx_url_template = 'http://cycling.waymarkedtrails.org/en/routebrowser/%s/gpx'

r = requests.get(wiki_url)
html = lxml.html.fromstring(r.text)
for span in html.xpath('//span[@title="browse relation"]'):
    route = span.xpath('ancestor::tr/td[position()=1]')[0].text_content().strip()
    gpx_url = gpx_url_template % span.text_content().strip()

    fn = '%s.gpx' % route
    if os.path.exists(fn):
        sys.stdout.write('Already downloaded gpx for route %s\n' % route)
        continue

    sys.stdout.write('Downloading gpx for route %s\n' % route)
    r = requests.get(gpx_url)
    if not r.ok:
        sys.stdout.write('Could not download %s\n' % zipped_track)
        continue
    with open(fn, 'wb') as fp:
        fp.write(r.content)
