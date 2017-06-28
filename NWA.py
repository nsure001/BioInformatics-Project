matchScore = int(raw_input("Match Score = "));
gapScore = int(raw_input("Gap Score = "));
mismatchScore = int(raw_input("Mismatch Score = "));

 
m=0
n=0
matchscore=1
mismatchscore=0
gapscore=-1

a1=open("fasta1.txt",'r')
seq1=""
count=0
for s1 in a1:
	if count!=0:
		s1 = s1[:-1]
		seq1+=s1
	count+=1
seq2=""
count=0
a2=open("fasta2.txt",'r')
for s2 in a2:
	if count!=0:
		s2 = s2[:-1]
		seq2+=s2
	count+=1
	
cells = {}
 
globalBestScore = [None, -100000]
 
def getAnAlignCell(p, q, seq1, seq2):
    
    def alnCell():
 
        global globalBestScore
        global cells
 
        b1, b2 = seq1[p], seq2[q] 
        mp, mq = len(seq1), len(seq2)
        
        count = 0
 
        cellData = []
 
        if p == 0 or q == 0:
            cellId, s = yield
            cellData.append( (cellId, s) )
        else:
            cellId, s = yield
            cellData.append( (cellId, s) )
            cellId, s = yield
            cellData.append( (cellId, s) )
            cellId, s = yield
            cellData.append( (cellId, s) )
 
        cellData.sort( key=lambda p: -p[1] )
        bestCell, bestScore = cellData[0]
 
        if bestScore > globalBestScore[1]:
            globalBestScore = [ (p,q), bestScore ]
 
        if p+1 < mp and q+1 < mq:
            
            if (p+1, q+1) not in cells:
                cells[ (p+1, q+1) ] = getAnAlignCell( p+1, q+1, seq1, seq2 )()
                cells[ (p+1, q+1) ].next() 
            if b1 == b2: 
                cells[ (p+1, q+1) ].send( ((p,q), bestScore + matchScore) ) 
            else: 
                cells[ (p+1, q+1) ].send( ((p,q), bestScore + mismatchScore) ) 
        if p+1 < mp:
            
            if (p+1, q) not in cells:
                cells[ (p+1, q) ] = getAnAlignCell( p+1, q, seq1, seq2 )()
                cells[ (p+1, q) ].next() 
            cells[ (p+1, q) ].send( ((p,q), bestScore + gapScore) )
        
        if q+1 < mq:
            
            if (p, q+1) not in cells:
                cells[ (p, q+1) ] = getAnAlignCell( p, q+1, seq1, seq2 )()
                cells[ (p, q+1) ].next() 
            cells[ (p, q+1) ].send( ((p,q), bestScore + gapScore) )
             
        path = yield  
         
        if bestCell[0] >= 0 and bestCell[1] >=0 :
            if path == None:
                path = []
             
            if bestCell[0] - p == 0:
                y1 = "-"
            else:
                y1 = seq1[p-1]
            if bestCell[1] - q == 0:
                y2 = "-"
            else:
                y2 = seq2[q-1]
            path.extend( [ (y1, y2) ] ) 
            if y1 == y2:
                count += 1
            
            cells[ bestCell ].send(  path   )
            print count
                 
        yield path
 
    return alnCell
 
cells[ (0,0) ] = getAnAlignCell( 0, 0, seq1, seq2 )()

cells[(0,0)].next()

cells[(0,0)].send( ( (-1, -1), 0 ) )

bestCell = globalBestScore[0]

bestPath = cells[bestCell].next()
bestPath.reverse()
 
alnRes = zip(*bestPath)
print "".join(alnRes[0])
print "".join(alnRes[1])