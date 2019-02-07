#!/usr/bin/python

from __future__ import with_statement
from __future__ import absolute_import
import sys
from io import open

if (len(sys.argv) != 3):
	sys.exit(u"Usage: " + sys.argv[0] + u" [ascii-art-in] [payload-out]")

inname = sys.argv[1]
outname = sys.argv[2]

infile = open(inname, u"r")
outfile = open(outname, u"w")
with open(u"altcodes.txt", u"r") as f:
	altcodes = f.readlines()

# Write start of file
outfile.write(u"LED SETUP\nATTACKMODE HID\nLED ATTACK\nQUACK GUI r\nQUACK DELAY 500\nQUACK STRING \"cmd /K copy con ansi.txt&exit\"\nQUACK ENTER\nQUACK DELAY 1000\n\n")

# 'Compile' to ALT-Codes and append to file
for line in infile:
	newline = u""
	for char in line:
		for altline in altcodes:
			if char in altline.strip().split(u" ")[-1]:
				newline += u"QUACK ALTCODE " + unicode(altline.strip().split(u" ")[0]) + u"\n"
	outfile.write(newline + u"QUACK enter\n\n")

print u"Payload written to " + outname