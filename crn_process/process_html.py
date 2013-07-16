#!/usr/bin/python
""" This script intends to process the raw html file
to extract out course name, course number, and crn """

import bs4

input = open('/home/ltae9110/Desktop/orig.html', 'rb') # open input file
raw_html = input.read()
input.close()


print bs4.BeautifulSoup(raw_html)			# invoke BS4 to process html



