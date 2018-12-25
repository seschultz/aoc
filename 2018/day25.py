points=[]

inConst=[]

myConst=[]

with open('in25.txt') as inFile:
    for l in inFile:
        n=l.rstrip().split(',')
        n = list(map(int, n))
        points.append(n)
        
def dist(p1,p2):
    return abs(p1[0]-p2[0])+abs(p1[1]-p2[1])+abs(p1[2]-p2[2])+abs(p1[3]-p2[3])

n=0
while len(inConst)<len(points):
    for point in points:
        if point not in inConst:
            inConst.append(point)
            myConst.append(point)
            for othPoint in points:
                if point!=othPoint and dist(point,othPoint)<=3:
                    inConst.append(othPoint)
                    myConst.append(othPoint)
            added=1
            while added>=1:
                added=0
                for mPoint in myConst:
                    for othPoint in points:
                        if othPoint not in myConst and dist(othPoint,mPoint)<=3:#othPoint!=mPoint and point!=mPoint and dist(mPoint,othPoint)<=3:
                            inConst.append(othPoint)
                            myConst.append(othPoint)
                            added+=1
            #shouldn't be empty now anyway, but left in just cuz
            if myConst!=[]:
                n+=1
            myConst=[]
       
#solution
print(n)