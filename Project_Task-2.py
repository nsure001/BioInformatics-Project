from decimal import Decimal
from collections import Counter

import math
import sys

def T_1():
	
	ipfile = open(fname,"r")
	opfile = open("result1.pdb","w")
	strg = ["O", "H", "C", "N", "CA"]
	bline = []
	natoms=0
	par = 0
	xs = ys = zs = 0
	counter = 0
	m = ""
	p = 1
	
	
	for line in ipfile:
		line = line.split()
		
		if "ATOM" in line[0]:
			
			if len(line[2]) > 3:
				n = line[2][3:]
				line.insert(3,n)
				t = line[2][:3]
				line[2] = t
			
			if line[2] not in strg:
				if par != int(line[5]):
					if natoms != 0:
					
						remavg = remsum/ natoms
						xa = xs/ natoms
						ya = ys/ natoms
						za = zs/ natoms
						
						m = bline[5]
						
						x = str(round(Decimal(xa),3))
						y = str(round(Decimal(ya),3))
						z = str(round(Decimal(za),3))
						w = str(round(Decimal(remavg),2))
						
						opfile.write( "ATOM" + (6 - len(str(p))) * " " + str(p) + "  S   " + str(bline[3]) + " " + str(bline[4]) + (4 - len(str(m))) * " " + str(m) + (12 - len(x)) * " " + x + (8 - len(y)) * " " + y + (8 - len(z)) * " " + z + "  1.00 " + str(w) + (16 - len(str(w))) * " " + "S" + "\n")
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
	
	opfile.write("ATOM" + (6 - len(str(p))) * " " + str(p) + "  S   " + str(bline[3]) + " " + str(bline[4]) + (4 - len(str(m))) * " " + str(m) + (12 - len(x)) * " " + x + (8 - len(y)) * " " + y + (8 - len(z)) * " " + z + "  1.00 " + str(w) + (16 - len(str(w))) * " " + "S" + "\n")
	
	print "1. Output filename: result1.pdb"
	opfile.close()
	
	
def T_2():

	ipfile= open(fname,"r")
	
	
	arr1 = {}
	h = []
	keys = []

	for lines in ipfile:
		lines = lines.split()
		if lines[0] == "HELIX":
			h.append(lines)
	
	ipfile= open(fname,"r")
	for line in ipfile:
		line = line.split()
		
		if line[0] == "ATOM":
			
			if len(line[2]) > 3:
				n = line[2][3:]
				line.insert(3,n)
				t = line[2][:3]
				line[2] = t
			
			if line[2] == "CA":	
				if int(line[5]) not in arr1.keys():
					arr1[int(line[5])] = line
					keys.append(int(line[5]))

		
	opfile = open('result2.pdb',"w")	
	p = 1

	for line in h:
		start = int(line[5])
		stop = int(line[8])
		
		for i in arr1.keys():
			x = y = z = w = 0
			
			if i >= start and i <= stop - 3:
				q = keys.index(i)
				
				x +=  float(arr1[i][6]) + float(arr1[keys[q + 1]][6]) + float(arr1[keys[q + 2]][6]) + float(arr1[keys[q + 3]][6])
				y +=  float(arr1[i][7]) + float(arr1[keys[q + 1]][7]) + float(arr1[keys[q + 2]][7]) + float(arr1[keys[q + 3]][7])
				z +=  float(arr1[i][8]) + float(arr1[keys[q + 1]][8]) + float(arr1[keys[q + 2]][8]) + float(arr1[keys[q + 3]][8])
				w +=  float(arr1[i][10]) + float(arr1[keys[q + 1]][10]) + float(arr1[keys[q + 2]][10]) + float(arr1[keys[q + 3]][10])
				
				x = round(x/ 4,3)
				y = round(y/ 4,3)
				z = round(z/ 4,3)
				w = round(w/ 4,3)
				
				x = str(x)
				y = str(y)
				z = str(z)
				w = str(w)
				
				
				opfile.write("ATOM" + (6 - len(str(p))) * " " + str(p) + "  S   " + str(arr1[i][3]) + " " + str(arr1[i][4]) + (4 - len(str(arr1[i][5]))) * " " + str(arr1[i][5]) + (12 - len(x)) * " " + x + (8-len(y)) * " " + y + (8 - len(z)) * " " + z + "  1.00 " + str(w) + (16 - len(str(w))) * " " + "S" + "\n")
				
				p+= 1
			
	print "2. Output filename: result2.pdb"	
	opfile.close()
	

	
def T_3():	

	ipfile = open(fname,"r")
	
	p = 1
	m = 0
	store ={}
	keys1 =[]
	arr2 = []
	arr3 = []
	arr4 = []
	
	for line in ipfile:
		arr3 = line.split()
		
		if arr3[0] == "SHEET":
			start = arr3[6]
			stop = arr3[9]
			arr4.append(start)
			arr4.append(stop)
			
	ipfile.close()
	
	ipfile1 = open(fname,"r")
	ipfile1.readline()
	
		
	for line in ipfile1:
		arr2 = line.split()
	
		if arr2[0] == "ATOM":
			
			if arr2[2] == "N" or arr2[2] == "CA" or arr2[2] == "C":
				
				if int(arr2[5]) not in store.keys():
					
					store[int(arr2[5])] = [arr2]
					
				else:
					store[int(arr2[5])].append(arr2)
					
				
				if int(arr2[5]) not in keys1:
					
					keys1.append(int(arr2[5]))
	
	opfile = open('result3.pdb','w')
	

	for i in range(0,len(arr4),2):
		
		for j in store.keys():
			
			if int(store[j][0][5]) >= int(arr4[i]) and  int(store[j][0][5]) <= int(arr4[i + 1]):
				
				q = keys1.index(int(store[j][0][5]))
				
				try:
		
					x=  round((float(store[j][0][6])+ float(store[j][1][6]) + float(store[j][2][6]) + float(store[keys1[q + 1]][0][6]))/4,3)
			
					y=  round((float(store[j][0][7])+ float(store[j][1][7]) + float(store[j][2][7]) + float(store[keys1[q + 3]][0][7]))/4,3)
			
					z=  round((float(store[j][0][8])+ float(store[j][1][8]) + float(store[j][2][8]) + float(store[keys1[q + 3]][0][8]))/4,3)
			
					w=  round((float(store[j][0][10])+ float(store[j][1][10]) + float(store[j][2][10]) + float(store[keys1[q + 3]][0][10]))/4,3)
			
					
					x = str(x)
					y = str(y)
					z = str(z)
					w = str(w)
					
					
					opfile.write( "ATOM" + (6 - len(str(p))) * " " + str(p) + "  S   " + str(store[j][0][3]) + " " + str(store[j][0][4]) + (4 - len(str(store[j][0][5]))) * " " + str(store[j][0][5]) + (12 - len(x)) * " " + x + (8 - len(y)) * " " + y + (8 - len(z)) * " " + z + "  1.00 " + str(w) + (16 - len(str(w))) * " " + "S" + "\n" )
					p+= 1
					
				except:
					m = 1
	
	print "3. Output filename: result3.pdb"
	opfile.close()

	
#Filename given by user
fname = raw_input("Name of the input pdb file: ")		

#Calling all the functions
print "--------------------Executing all the tasks--------------------"
T_1()
T_2()
T_3()