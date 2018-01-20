# -*- coding: utf-8 -*-
"""
Your task in this exercise has two steps:

- audit the OSMFILE and change the variable 'mapping' to reflect the changes needed to fix 
    the unexpected street types to the appropriate ones in the expected list.
    You have to add mappings only for the actual problems you find in this OSMFILE,
    not a generalized solution, since that may and will depend on the particular area you are auditing.
- write the update_name function, to actually fix the street name.
    The function takes a string with street name as an argument and should return the fixed name
    We have provided a simple test so that you see what exactly is expected
"""
import xml.etree.cElementTree as ET
from collections import defaultdict
import re
import pprint

OSMFILE = "map"
zip_code_re = re.compile(r'^\d{5}(?:[-\s]\d{4})?$')
bad_zips =[]
corrected_zips = []

# UPDATE THIS VARIABLE
zipMap = { "MA 02116": "02116",
			"MA 02118": "02118",
			"MA 02135": "02135",
                        }

#Entries that don't correspond to Boston Zipcodes
ignored = ["MA","MA 02186","MA 02453", "01908-14ND", "2451"]


#identifies zipcodes
def is_zipcode(elem):
	return (elem.attrib['k'] == 'addr:postcode')


#function to clean zipcodes, create list of improper codes and update those with poor formatting within the boston area
def audit_zipcode(zipcode):

	zipcode_split = zipcode.strip() #separate chars
	m = zip_code_re.search(zipcode_split)
	if m:
		return zipcode
	elif zipcode not in ignored:
		bad_zips.append(zipcode)
		zipcode = zipMap[zipcode]		
		corrected_zips.append(zipcode)

#Iterate and catch bad zipcodes
def zip_audit():

	for event, elem in ET.iterparse(OSMFILE, events=("start",)):
		if elem.tag =="node" or elem.tag == "way":
			for tag in elem.iter("tag"):
				if is_zipcode(tag):
					audit_zipcode(tag.attrib['v'])
	print "Poorly formatted Zip Codes: "
	pprint.pprint(bad_zips)
	print "Corrected: "
	pprint.pprint(corrected_zips)

def update_zip(zipcode, mapping):

    m = zip_code_re.search(zipcode)
    if m:
        zip_code = m.group()
        if zip_code in zipMap:
            zipcode = re.sub(zip_code_re, zipMap[zip_code], zipcode)

    return zipcode


					
#Commented to treat as module in data.py. Uncomment if using as standalone
#zip_audit()
