import numpy as np

largest=0

largestCoord=[0,0]

#puzzle input
serial=6548

#extra row and column since puzzle has 1-indexing
grid=np.zeros((301,301))

for i in range(301):
    for j in range(301):

        p=((i+10)*j+serial)*(i+10)
        
        s=str(p)
        if len(s)<3:
            pl=0
        else:
            pl=s[-3]
            
        grid[i,j]=int(pl)-5
        
for i in range(1,301-3):
    for j in range(1,301-3):
       
        totalPower=np.sum(grid[i:i+3,j:j+3])
        
        if totalPower>largest:
            largest=totalPower
            largestCoord=[i,j]

        
print(largest)
#answer part 1
print(largestCoord)

#this is pretty slow, takes a few minutes
for i in range(1,301):
    for j in range(1,301):
        
        maxSize=min((301-i),(301-j))
                
        for k in range(maxSize+1):
            totalPower=np.sum(grid[i:i+k,j:j+k])
                        
            if totalPower>largest:
                largest=totalPower
                largestCoord=[i,j,k]
            
print(largest)
#answer part 2
print(largestCoord)