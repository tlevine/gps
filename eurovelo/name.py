#!/usr/bin/env python3
import os

import lxml.etree

NS = {'gpx': 'http://www.topografix.com/GPX/1/1'}

for fn in os.listdir():
    if not fn.endswith('gpx'):
        continue
    route = fn.partition('.')[0]
    gpx = lxml.etree.parse(fn)
    for i, trk in enumerate(gpx.xpath('//gpx:trk', namespaces = NS)):
        name = lxml.etree.Element('name')
        name.text = '%s.%d' % (route, i)
        trk.append(name)
    break
