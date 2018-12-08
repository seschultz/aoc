import copy

c=[]
n=[]

with open("in7.txt") as file:
    for l in file:
        condition=l[5]
        c.append(condition)
        nextS=l[-13]
        n.append(nextS)

n2=copy.deepcopy(n)

def avail(n):
    av={}
    for l in ascii_uppercase:
        if l not in n:
            av[l]=True
        else:
            av[l]=False
    return av
        
def chooseAct(av):
    for l in ascii_uppercase:
        if av[l]==True:
            return l

order=''
for i in range(26):
    available=avail(n)   

    for char in order:
        available[char]=False
    
    c1=(chooseAct(available))
        
    order+=c1
    
    for j in range(len(c)):
        if c[j]==c1:
            n[j]='.'
            
#answer part 1
print(order)

def time(char):
    return ord(char)-4

countdown=[0,0,0,0,0]

working=[0,0,0,0,0]


newOrder=''
done=0
i=0
while done<26:
    available=avail(n2)
    
    for k in range(5):
        if working[k]!=0:
            available[working[k]]=False

    for char in newOrder:
        available[char]=False
    
    for m in range(5):
        if countdown[m]==0:
            n1=chooseAct(available)
            if n1!=None:
                working[m]=n1
                countdown[m]=time(n1)
                available[n1]=False
    
    countdown[:] = [x - 1  if x > 0 else x for x in countdown]
    
    for k in range(5):
        if countdown[k]==0 and working[k]!=0:
            newOrder+=working[k]
            done+=1
            for j in range(len(c)):
                if c[j]==working[k]:
                    n2[j]='.'
            working[k]=0

    i+=1

#answer to part 2
print(i)