#!/usr/bin/env python
# http://en.nederlandfietsland.nl/en/long-distance-cycle-routes/gps-tracks
import sys, os

import lxml.html, requests

url = 'http://wiki.openstreetmap.org/wiki/WikiProject_Europe/EuroVelo'
r = requests.get(url)
html = lxml.html.fromstring(r.text)
html.make_links_absolute(url)
for anchor in html.xpath('//a[text()="gpx"]'):
    route = anchor.xpath('ancestor::tr/td[position()=1]')[0].text_content().strip()
    fn = '%s.gpx' % route
    if os.path.exists(fn):
        sys.stdout.write('Already downloaded gpx for route %s\n' % route)
        continue
    sys.stdout.write('Downloading gpx for route %s\n' % route)
    zipped_track = anchor.xpath('@href')[0]
    r = requests.get(zipped_track)
    if not r.ok:
        sys.stdout.write('Could not download %s\n' % zipped_track)
        continue
    with open(fn, 'wb') as fp:
        fp.write(r.content)
