import numpy as np

pos=[]

vels=[]

origGrid=np.chararray((110000, 110000))
origGrid[:]='.'

numPoints=0

with open('in10.txt') as file:
    for l in file:
        xP=int(l[10:l.index(',')])
        yP=int(l[l.index(',')+1:l.index('>')])
                
        yV=int(l[-4:-2])
        xV=int(l[-8:-6])
        
        pos.append([xP,yP])
        
        vels.append([xV,yV])
        
        numPoints+=1
  
    
grid=origGrid
    
center=[55000,55000]
    
grid[:] = '.'
              
def printMsg(pos,n):
    
    pos=np.array(pos)
    
    sizeX=max(pos[:,0])-min(pos[:,0])
    sizeY=max(pos[:,1])-min(pos[:,1])
        
    if sizeX<numPoints and sizeY%9==0:
        #print(numPoints)
        print(sizeX,sizeY,n)
        for i in range(len(pos)):
            grid[center[0]+pos[i][0]][center[1]+pos[i][1]]='#'
            
        outg=(grid[center[0]+min(pos[:,0]):center[0]+max(pos[:,0])+1,center[1]+min(pos[:,1]):center[1]+max(pos[:,1])+1].transpose())
        
        np.savetxt("output"+str(n)+".txt", 
                   outg,
                       delimiter=" ", fmt='%s')

ret=False
n=0
while not ret and n<20000:    
    
    for item in range(len(pos)):
        pos[item][0]+= vels[item][0]
        pos[item][1]+= vels[item][1]
    
    printMsg(pos,n)
    n+=1

#find smallest output file and read out answer (find replace ' and b with nothing, change to consistent-size font)
#its num+1 is answer part 2