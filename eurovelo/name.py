#!/usr/bin/env python3
import os, xml.etree


for fn in os.listdir():
    if fn.endswith('gpx'):
        continue
    gpx = xml.etree.ElementTree.parse('EV1.gpx').getroot()
    break
