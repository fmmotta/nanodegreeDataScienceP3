#!/usr/bin/env python

import xml.etree.cElementTree as ET
import pprint



def count_tags(filename):
    d = {}
    for event, elem in ET.iterparse(filename):
        if elem.tag in d:
            d[elem.tag] += 1
        else:
            d[elem.tag] = 1
    return d

print(count_tags('map'))
