from decimal import Decimal
from collections import Counter

import math
import sys
fname = raw_input("Name of the input file: ")

def T_1():
	natoms=0
	par = 0
	xs = ys = zs = 0
	counter = 0
	
	m = ""
	
	ipfile = open(fname,"r")
	opfile = open("result1.pdb","w")
	strings = ["O", "H", "C", "N", "CA"]
	bline = []
	
	p = 1
	for line in ipfile:
		line = line.split()
		if 'ATOM' in line[0]:
			if len(line[2]) > 3:
				n = line[2][3:]
				line.insert(3,n)
				t = line[2][:3]
				line[2] = t
			
			if line[2] not in strings:
				if par != int(line[5]):
					if natoms != 0:
					
						remavg = remsum / natoms
						xa = xs / natoms
						ya = ys / natoms
						za = zs / natoms
						
						m = bline[5]
						
						x = str(round(Decimal(xa),3))
						y = str(round(Decimal(ya),3))
						z = str(round(Decimal(za),3))
						w = str(round(Decimal(remavg),2))
						
						opfile.write( "ATOM" + (6 - len(str(p))) * " " + str(p) + "  S   " + str(bline[3]) + " " + str(bline[4]) + (4 - len(str(m))) * " " + str(m) + (12 - len(x)) * " " + x + (8 - len(y)) * " " + y + (8 - len(z)) * " " + z + "  1.00 " + str(w) + (16 - len(str(w))) * " " + "C" + "\n")
						p += 1
						
						xa = ya = za = remavg = 0
					
					par = int(line[5])
					
					natoms = 1
					
					xs = float(line[6])
					ys = float(line[7])
					zs = float(line[8])
					remsum = float(line[10])
					
					
				else:
					natoms = natoms+1
					
					xs = xs+float(line[6])
					ys = ys+float(line[7])
					zs = zs+float(line[8])
					remsum = remsum+float(line[10])
				
				bline = line
				
	xa = xs/natoms
	ya = ys/natoms
	za = zs/natoms
	remavg = remsum/natoms
	
	m = bline[5]
	
	x = str(round(Decimal(xa),3))
	y = str(round(Decimal(ya),3))
	z = str(round(Decimal(za),3))
	w = str(round(Decimal(remavg),2))
	
	opfile.write("ATOM" + (6 - len(str(p))) * " " + str(p) + "  S   " + str(bline[3]) + " " + str(bline[4]) + (4 - len(str(m))) * " " + str(m) + (12 - len(x)) * " " + x + (8 - len(y)) * " " + y + (8 - len(z)) * " " + z + "  1.00 " + str(w) + (16 - len(str(w))) * " " + "C" + "\n")
	
	opfile.close()
	print "\t\t***result1.pdb is generated.***"
	
def T_2():

	ipfile= open(fname,"r")
	opfile = open('result2.pdb','w')
	
	arr1 = {}
	h = []
	keys = []

	for lines in ipfile:
		lines = lines.split()
		if lines[0] == 'HELIX':
			h.append(lines)
	ipfile= open(fname,"r")
	for line in ipfile:
		line = line.split()
		if line[0] == 'ATOM':
			if len(line[2]) > 3:
				n = line[2][3:]
				line.insert(3,n)
				t = line[2][:3]
				line[2] = t
			if line[2] == 'CA':	
				if int(line[5]) not in arr1.keys():
					arr1[int(line[5])] = line
					keys.append(int(line[5]))

		
		
	p = 1

	for line in h:
		begin = int(line[5])
		end = int(line[8])
		for i in arr1.keys():
			x = y = z = w = 0
			
			if i >= begin and i <= end -3:
				a = keys.index(i)
				
				x +=  float(arr1[i][6]) + float(arr1[keys[a + 1]][6]) + float(arr1[keys[a + 2]][6]) + float(arr1[keys[a + 3]][6])
				y +=  float(arr1[i][7]) + float(arr1[keys[a + 1]][7]) + float(arr1[keys[a + 2]][7]) + float(arr1[keys[a + 3]][7])
				z +=  float(arr1[i][8]) + float(arr1[keys[a + 1]][8]) + float(arr1[keys[a + 2]][8]) + float(arr1[keys[a + 3]][8])
				w +=  float(arr1[i][10]) + float(arr1[keys[a + 1]][10]) + float(arr1[keys[a + 2]][10]) + float(arr1[keys[a + 3]][10])
				
				x = round(x / 4,3)
				y = round(y / 4,3)
				z = round(z / 4,3)
				w = round(w / 4,3)
				
				x = str(x)
				y = str(y)
				z = str(z)
				w = str(w)
				
				
				opfile.write("ATOM" + (6 - len(str(p))) * " " + str(p) + "  S   " + str(arr1[i][3]) + " " + str(arr1[i][4]) + (4 - len(str(arr1[i][5]))) * " " + str(arr1[i][5]) + (12 - len(x)) * " " + x + (8-len(y)) * " " + y + (8 - len(z)) * " " + z + "  1.00 " + str(w) + (16 - len(str(w))) * " " + "S" + "\n")
				
				p += 1
			
		
	opfile.close()
	print "\t\t***result2.pdb is generated.***"

	
def T_3():	

	ipfile = open(fname,"r")
	opfile = open('result3.pdb',"w")

	arr3 = {}
	keys = []
	for line in ipfile:
		line = line.split()
		if line[0] == 'ATOM':
			if len(line[2]) > 3:
				n = line[2][3:]
				line.insert(3,n)
				t = line[2][:3]
				line[2] = t
			if int(line[5]) not in arr3.keys():
				arr3[int(line[5])] = []
				arr3[int(line[5])].append(line)
				keys.append(int(line[5]))
			else:
				arr3[int(line[5])].append(line)
				
	p = 1

	for i in arr3.keys():
		length = len(arr3.keys())-1 
		if i != arr3.keys()[length]:
		
			x = y = z = w = 0
			a = keys.index(i)
			
			x +=  float(arr3[i][0][6]) + float(arr3[i][1][6]) + float(arr3[i][2][6]) + float(arr3[keys[a+1]][0][6])
			y +=  float(arr3[i][0][7]) + float(arr3[i][1][7]) + float(arr3[i][2][7]) + float(arr3[keys[a+1]][0][7])
			z +=  float(arr3[i][0][8]) + float(arr3[i][1][8]) + float(arr3[i][2][8]) + float(arr3[keys[a+1]][0][8])
			w +=  float(arr3[i][0][10]) + float(arr3[i][1][10]) + float(arr3[i][2][10]) + float(arr3[keys[a+1]][0][10])
			x = round(x/4,3)
			y = round(y/4,3)
			z = round(z/4,3)
			w = round(w/4,3)
			x = str(x)
			y = str(y)
			z = str(z)
			w = str(w)
			opfile.write("ATOM" + (6 - len(str(p))) * " " + str(p) + "  S   " + str(arr3[i][0][3]) + " " + str(arr3[i][0][4]) + (4 - len(str(arr3[i][0][5]))) * " " + str(arr3[i][0][5]) + (12-len(x)) * " " + x + (8 - len(y)) * " " + y + (8 - len(z)) * " " + z + "  1.00 " + str(w) + (16 - len(str(w))) * " " + "S" + "\n")
			p += 1
				
		
	opfile.close()
	print "\t\t***result3.pdb is generated.***"
	
	
T_1()
T_2()
T_3()
