import numpy as np

xs=[]
ys=[]

with open("in6.txt") as file:
    for l in file:
        s=l.split(',')
        xs.append(int(s[0]))
        ys.append(int(s[1]))


maxX=max(xs)
maxY=max(ys)

maps=np.zeros((maxX+1,maxY+1))

for i in range(len(xs)):
    maps[xs[i],ys[i]]=i+1
    
cs=[]
infs=[]

for x in range(maxX+1):
    for y in range(maxY+1):
        smallest=700
        choice=-1
        tie=False
        if maps[x][y]==0:
            for j in range(len(xs)):
                xDif=abs(xs[j]-x)
                yDif=abs(ys[j]-y)
                dist=xDif+yDif
                if dist==smallest:
                    tie=True
                if dist<smallest:
                    tie=False
                    smallest=dist
                    choice=j
            if tie:
                maps[x][y]=-1
            else:
                maps[x][y]=choice
                if x==0 or y==0 or x==maxX or y==maxY:
                    if choice not in infs:
                        infs.append(choice)
                cs.append(choice)
        else:
            cs.append(maps[x][y])
            
a=np.bincount(cs)
a[infs]=0
#answer to part 1
print(max(a))

map2=np.zeros((maxX+1,maxY+1))

for x in range(maxX+1):
    for y in range(maxY+1):
        totalDist=0
        for j in range(len(xs)):
            totalDist+=abs(xs[j]-x)+abs(ys[j]-y)
        if totalDist<10000:
            map2[x][y]=1

#answer to part 2 (expected this to be too big since i didn't actually check
#that it was continous, but turns out to be correct)
print(np.count_nonzero(map2))

