#!/usr/bin/python

A1 = raw_input("Input Protein Structure file:")
inputfile = A1 + ".pdb"
psinput  = open(inputfile,"r")
psoutput = open("PT1.pdb","w")

psinput.readline()
for line in psinput:
	if 'ATOM' in line:
		if 'CA' in line:
			psoutput.write(line)

