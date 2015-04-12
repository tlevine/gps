#!/usr/bin/env python3
import os, sys, re
from concurrent.futures import ThreadPoolExecutor

import lxml.etree

def main():
    with ThreadPoolExecutor(4) as e:
        for fn in os.listdir():
            if re.match(r'^[EV0-9]+\.gpx$', fn):
                sys.stdout.write('Submitting %s\n' % fn)
                e.submit(convert_file, fn)

def convert_file(old_fn):
    basename = old_fn.partition('.')[0]
    gpx = lxml.etree.iterparse(old_fn)
    i = 1

    for end, element in gpx:
        if not element.tag == '{http://www.topografix.com/GPX/1/1}trk':
            continue
        new_fn = '%s.%04d.gpx' % (basename, i)
        i += 1
        with open(new_fn, 'wb') as fp:
            fp.write(lxml.etree.tostring(convert_trk(element)))

def convert_trk(trk):
    gpx = lxml.etree.fromstring(b'''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <gpx version="1.1" creator="GPS Utility 4.20 - http://www.gpsu.co.uk"
      xmlns="http://www.topografix.com/GPX/1/1"
      xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
      xsi:schemaLocation="http://www.topografix.com/GPX/1/1 http://www.topografix.com/GPX/1/1/gpx.xsd">
</gpx>
''')
    gpx.append(trk)
    return gpx

if __name__ == '__main__':
    main()
