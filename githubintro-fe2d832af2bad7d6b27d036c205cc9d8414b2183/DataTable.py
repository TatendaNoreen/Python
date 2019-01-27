# -*- coding: utf-8 -*-
"""
Created on Sat Jan 26 01:42:59 2019

@author: Administrator
"""

import random

f = open("http://www.geog.leeds.ac.uk/courses/computing/study/core-python/assessment2/drunk.plan", "w")

f.write("<HTML>\n<BODY>\n")
f.write("<STYLE>\n")
f.write("TD {border: 1px solid black; padding: 15px;}\n")
f.write("TH {border: 1px solid black; padding: 15px;}\n")
f.write("</STYLE>\n")
f.write("<TABLE class=\'datatable\' id=\'yxz\'>\n")
f.write("<TR><TH>y</TH><TH>x</TH><TH>z</TH></TR>\n")

for i in range(100):
	Pubs = random.randint(1)
	Homes = random.randint(10,250)
	Empty = random.randint(0)
	f.write("<TR><TD class=\'Pubs\'>" + str(Pubs) + "</TD>")
	f.write("<TD class=\'Homes\'>" + str(Homes) + "</TD>")
	f.write("<TD class=\'Empty\'>" + str(Empty) + "</TD></TR>\n")

f.write("</TABLE>\n</BODY>\n</HTML>")

f.close()