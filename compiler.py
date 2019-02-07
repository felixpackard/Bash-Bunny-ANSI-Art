#!/usr/bin/python

import sys

if (len(sys.argv) != 3):
	sys.exit("Usage: " + sys.argv[0] + " [ascii-art-in] [payload-out]")

inname = sys.argv[1]
outname = sys.argv[2]

infile = open(inname, "r")
outfile = open(outname, "w")
with open("altcodes.txt", "r") as f:
	altcodes = f.readlines()

# Write start of file
outfile.write("LED SETUP\nATTACKMODE HID\nLED ATTACK\nQUACK GUI r\nQUACK DELAY 500\nQUACK STRING \"cmd /K copy con ansi.txt&exit\"\nQUACK ENTER\nQUACK DELAY 1000\n\n")

# 'Compile' to ALT-Codes and append to file
for line in infile:
	newline = ""
	for char in line:
		for altline in altcodes:
			if char in altline.strip().split(" ")[-1]:
				newline += "QUACK ALTCODE " + str(altline.strip().split(" ")[0]) + "\n"
	outfile.write(newline + "QUACK enter\n\n")

print("Payload written to " + outname)