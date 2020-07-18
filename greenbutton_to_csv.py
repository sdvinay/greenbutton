#!/usr/bin/env python
# coding: utf-8

import xml.etree.ElementTree as etree
import sys


tree = etree.parse(sys.argv[1])
root = tree.getroot()


for entry in root.findall('{http://www.w3.org/2005/Atom}entry'):
    for content in entry.findall('{http://www.w3.org/2005/Atom}content'):
        for interval_block in content.findall('{http://naesb.org/espi}IntervalBlock'):
            for reading in interval_block.findall('{http://naesb.org/espi}IntervalReading'):
                tp = reading.find('{http://naesb.org/espi}timePeriod')
                duration = tp.find('{http://naesb.org/espi}duration').text
                start    = tp.find('{http://naesb.org/espi}start').text
                value    = reading.find('{http://naesb.org/espi}value').text
                print(",".join([start, duration, value]))
