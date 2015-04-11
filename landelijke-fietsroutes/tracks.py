#!/usr/bin/env python
# http://en.nederlandfietsland.nl/en/long-distance-cycle-routes/gps-tracks
import lxml.html, requests

r = requests.get('http://en.nederlandfietsland.nl/en/long-distance-cycle-routes/gps-tracks')
html = lxml.html.fromstring(r.text)
print(html.xpath('//a[contains(".zip", @src)]/@src))
