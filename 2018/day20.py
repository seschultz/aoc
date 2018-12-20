import numpy as np
import copy

with open('in20.txt') as file:
    r=file.read().rstrip()

myMap=np.zeros((201,201))
myPos=[100,100]

saveSpots=[]

counter=0

saveCounters=[]

dists={}

for c in r:
    
    if c=='(':
        saveSpots.append(copy.deepcopy(myPos))
        saveCounters.append(counter)
        
    elif c=='|':
        myPos=copy.deepcopy(saveSpots[-1])
        counter=saveCounters[-1]
        
    elif c==')':
        saveSpots.remove(saveSpots[-1])
        saveCounters.remove(saveCounters[-1])
        
    elif c=='N':
        myMap[myPos[0]-1,myPos[1]]=1
        myPos[0]-=2 
        counter+=1 #n/s door
    elif c=='S':
        myMap[myPos[0]+1,myPos[1]]=1
        myPos[0]+=2 
        counter+=1 #n/s door
    elif c=='W':
        myMap[myPos[0],myPos[1]-1]=2
        myPos[1]-=2
        counter+=1 #e/w door
    elif c=='E':
        myMap[myPos[0],myPos[1]+1]=2
        myPos[1]+=2
        counter+=1 #e/w door

    myMap[myPos[0],myPos[1]]=3 #room
    if str(myPos) not in dists or dists[str(myPos)]>counter:
        dists[str(myPos)]=counter
    
#answer part 1
max_value = max(dists.values())
print(max_value)

#answer part 2
print(sum(i >= 1000 for i in dists.values()))
