ins=[]

with open("in1.txt") as file:
    for l in file:
        ins.append(int(l))
        
#answer to part 1
print(sum(ins))        

def findFirstRepeat(ins):
    sums=[]
    for j in range(1000):
        for i in range(len(ins)):
            if len(sums)==0:
                sums.append(ins[i])
            #s=sum(ins[0:i+1])
            else:
                s=sums[-1]+ins[i]
                if s in sums:
                    return s
                else:
                    sums.append(s)
    return None
        

#answer to part 2
print(findFirstRepeat(ins))