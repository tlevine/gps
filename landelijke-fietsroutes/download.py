#!/usr/bin/env python
# http://en.nederlandfietsland.nl/en/long-distance-cycle-routes/gps-tracks
import zipfile, io, sys

import lxml.html, requests

url = 'http://en.nederlandfietsland.nl/en/long-distance-cycle-routes/gps-tracks'
r = requests.get(url)
html = lxml.html.fromstring(r.text)
html.make_links_absolute(url)
for zipped_track in html.xpath('//a[contains(@href, ".zip")]/@href'):
    r = requests.get(zipped_track)
    if not r.ok:
        sys.stderr.write('Could not download %s\n' % zipped_track)
        continue
    try:
        z = zipfile.ZipFile(io.BytesIO(r.content))
    except zipfile.BadZipFile:
        sys.stderr.write('%s is not a zip file, skipping\n' % zipped_track)
    else:
        z.extractall()
