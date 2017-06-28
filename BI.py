i=0
j=0
match=1
mismatch=0
gap=-1

f=open("seq1.txt",'r')
x=""
count=0
for lines in f:
	if count!=0:
		lines = lines[:-1]
		x+=lines
	count+=1
y=""
count=0
f1=open("seq2.txt",'r')
for lines1 in f1:
	if count!=0:
		lines1 = lines1[:-1]
		y+=lines1
	count+=1
	
print x
print y

def calculate(p,q):
	position=""
	#print p,q
	a=diagonal(p,q)
	b=top(p,q)
	c=left(p,q)
	if(max(a,b,c)==a):
		position="Diag"
	elif(max(a,b,c)==b):
		position="Top"
	elif(max(a,b,c)==c):
		position="Left"	
	return max(a,b,c),position
	
def diagonal(p,q):
	if(x[p-1]== y[q-1]):
		value=b[p-1][q-1]+match
		return 	value
	else: 
		value=b[p-1][q-1]+mismatch
		return value
		
def top(p,q):
	value=b[p-1][q]+gap
	return value
def left(p,q):
	value=b[p][q-1]+gap
	return value

	
	

#x=raw_input("Enter sequence 1")
#y=raw_input("Enter sequence 2")
#x="GACTTAC"
#y="CGTGAATTCAT"
m=len(y)+1
n=len(x)+1
b=[[0 for i in range (m)] for j in range(n)]
trace=[["Done" for i in range (m)] for j in range(n)]

for p in range(1,n):
	trace[p][0] = "Top"
for p in range(1,m):
	trace[0][p] = "Left"

print m,n

			
b[0][0]=0
for p in range(1,m):
	b[0][p]=b[0][p-1]+gap
for q in range(1,n):
	b[q][0]=b[q-1][0]+gap

for p in range(1,n):
	for q in range(1,m):
		final,position=calculate(p,q)
		b[p][q]=final
		trace[p][q]=position
	


b1=[[0 for i in range (m+1)] for j in range(n+1)]

b1[0][0]=0
b1[0][1]=0
b1[1][0]=0
for p in range(2,m+1):
	b1[0][p]=y[p-2]
for p in range(2,n+1):
	b1[p][0]=x[p-2]

for p in range(1,n+1):
	for q in range(1,m+1):
		b1[p][q]=b[p-1][q-1]



r=m+1
t=n+1
for p in range(n+1):
	for q in range(m+1):
		if(p==0 and q==0):
			b1[p][q]=0
		elif(p==0 and q==1):
			b1[p][q]=0
		elif(p==1 and q==0):
			b1[p][q]=0
		elif(p==0 and q!=1):
			b1[p][q]=y[q-2]
		elif(q==0 and p!=1):	
			b1[p][q]=x[p-2]
		elif((p!=0)and(q!=0)):
			b1[p][q]=b[p-1][q-1]


print "Scoring Matrix\n"
	
space = 6	
for p in range(n+1):
	for q in range(m+1):
		f = len(str(b1[p][q]))
		s = space - f
		print   s*" "+str(b1[p][q]),
	print
print	

trace1=[["-" for i in range (m+1)] for j in range(n+1)]

trace1[0][0]=0
trace1[0][1]=0
trace1[1][0]=0
for p in range(2,m+1):
	trace1[0][p]=y[p-2]
for p in range(2,n+1):
	trace1[p][0]=x[p-2]

for p in range(1,n+1):
	for q in range(1,m+1):
		trace1[p][q]=trace[p-1][q-1]

print "Trace Matrix\n"


for p in range(n+1):
	for q in range(m+1):
		if(p==0 and q==0):
			trace1[p][q]=0
		elif(p==0 and q==1):
			trace1[p][q]=0
		elif(p==1 and q==0):
			trace1[p][q]=0
		elif(p==0 and q!=1):
			trace1[p][q]=y[q-2]
		elif(q==0 and p!=1):	
			trace1[p][q]=x[p-2]
		elif((p!=0)and(q!=0)):
			trace1[p][q]=trace[p-1][q-1]
			
space =6
for p in range(n+1):
	for q in range(m+1):
		f = len(str(trace1[p][q]))
		s = space - f
		print str(trace1[p][q])+ s*" ",
	print
print


i=n
j=m
str1=""  ##y
str2=""  ##x
flag=0
count=0

while(flag==0):
	if trace1[i][j]=="Diag":
		count+=b1[i][j]
		i=i-1
		j=j-1
		str1+=y[j-1]
		str2+=x[i-1]
	elif trace1[i][j]=="Top":
		count+=b1[i][j]
		i=i-1
		str1+="_"
		str2+=x[i-1]
	elif trace1[i][j]=="Left":
		count+=b1[i][j]
		j=j-1
		str1+=y[j-1]
		str2+="_"
	elif trace1[i][j]=="Done":
		flag=1

print "Optimal score: "+ str(count)
	
print "Optimal Alignment"
	
print str1[::-1]
print
print str2[::-1]