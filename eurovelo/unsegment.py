import os

import lxml.etree

def main():
    for gpx_fn in os.listdir():
        if not gpx_fn.endswith('.gpx'):
            continue

        gpx = lxml.etree.iterparse('EV15.gpx')
        basename = gpx.partition('.')[0]
        i = 1

        for end, element in gpx:
            if not element.tag == '{http://www.topografix.com/GPX/1/1}trk':
                continue
            fn = 
            i += 1
            with open('%s.%d.gpx', 'wb') as fp:
                fp.write(lxml.etree.tostring(convert(element)))

def convert(trk):
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
