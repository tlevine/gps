import os
from concurrent.futures import ThreadPoolExecutor

import lxml.etree

def main():
    with ThreadPoolExecutor(4) as e:
        for fn in os.listdir():
            if fn.endswith('.gpx'):
                e.submit(convert_file, fn)

def convert_file(old_fn):
    gpx = lxml.etree.iterparse(old_fn)
    basename = gpx.partition('.')[0]
    i = 1

    for end, element in gpx:
        if not element.tag == '{http://www.topografix.com/GPX/1/1}trk':
            continue
        i += 1
        with open('%s.%d.gpx', 'wb') as fp:
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
