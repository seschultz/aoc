inp=[]

with open("in13.txt") as file:
    for l in file:
        inp.append(l.rstrip())
        
numCarts=0

for n in range(len(inp)):
    numCarts+=sum(1 for x in inp[n] if (x=='v' or x=='^' or x=='<' or x=='>'))

prev=inp

cr=0

cartPositions=[]

for i in range(len(inp)):
    for j in range(len(inp[i])):
        x=inp[i][j]
        if (x=='v' or x=='^' or x=='<' or x=='>'):
            cartPositions.append([i,j,x,0])  

def orderCarts(cartPositions):

    ys=[i[0] for i in cartPositions]  
    
    xs=[i[1] for i in cartPositions]
    
    ys.sort()
    
    xs.sort()
    
    orderedCarts=[]
    
    for i in ys:
        for j in xs:
            for c in cartPositions:
                if c[0]==i and c[1]==j and c not in orderedCarts:
                    orderedCarts.append(c)
                    
    return orderedCarts
                
while numCarts>1:
    
    cr+=1

    cartPositions=orderCarts(cartPositions)
    rem=[]

    for cart in range(numCarts):
        facing=cartPositions[cart][2]
        turn=cartPositions[cart][3]
        
        #move
        if facing=='v':
            cartPositions[cart][0]+=1
        if facing=='^':
            cartPositions[cart][0]-=1
        if facing=='<':
            cartPositions[cart][1]-=1
        if facing=='>':
            cartPositions[cart][1]+=1  
            
            
        comp=inp[cartPositions[cart][0]][cartPositions[cart][1]] 
        
        #check for crashes
        rs=[cartPositions[cart]]
        for ct1 in range(numCarts):
            if cartPositions[cart][0]==cartPositions[ct1][0] and cartPositions[cart][1]==cartPositions[ct1][1] and cart!=ct1:
                print("crash")
                rs.append(cartPositions[ct1])
        if len(rs)>1:
            for r1 in rs:
                rem.append(r1)

        if comp=='+':
            if turn==0:
                #turn left
                if facing=='>':
                    cartPositions[cart][2]='^'
                if facing=='<':
                    cartPositions[cart][2]='v'
                if facing=='^':
                    cartPositions[cart][2]='<'
                if facing=='v':
                    cartPositions[cart][2]='>'
            elif turn==2:
                #turn right
                if facing=='>':
                    cartPositions[cart][2]='v'
                if facing=='<':
                    cartPositions[cart][2]='^'
                if facing=='^':
                    cartPositions[cart][2]='>'
                if facing=='v':
                    cartPositions[cart][2]='<'
            
            cartPositions[cart][3]=(turn+1)%3  
        
        elif comp=='/':
            if facing=='>':
                cartPositions[cart][2]='^'
            if facing=='<':
                cartPositions[cart][2]='v'
            if facing=='^':
                cartPositions[cart][2]='>'
            if facing=='v':
                cartPositions[cart][2]='<'
                
        
        elif comp=='\\':
            if facing=='>':
                cartPositions[cart][2]='v'
            if facing=='<':
                cartPositions[cart][2]='^'
            if facing=='^':
                cartPositions[cart][2]='<'
            if facing=='v':
                cartPositions[cart][2]='>'
        
    #remove crashed carts
    for r in rem:
        #transpose first 2 coords of carts in first crash for answer part 1
        print("removing cart "+ str(cartPositions.index(r)) + ' ' + str(r), cr)
        cartPositions.remove(r)
    numCarts-=len(rem)#len(rs)

#transpose first 2 coords for answer part 2
print(cartPositions, cr)
                
                
                
                
                