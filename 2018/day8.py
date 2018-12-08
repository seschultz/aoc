with open("in8.txt") as file:
    #for l in file:
    n=file.read().split()
    n = list(map(int, n))
        
def rec(nums):
    
    if len(nums)<1:
        return 0,0
    
    children=nums[0]
    meta=nums[1]
    
    f=0
    l=2
    
    if children==0:
        return sum(nums[2:2+meta]), 2+meta
    
    else:
        for i in range(children):
            m,li=rec(nums[l:])
            
            f+=m
            l+=li
         
        f+=sum(nums[l:l+meta])
            
        return f,l+meta  
      
#answer part 1
print(rec(n)[0])

def rec2(nums):
    
    f=0
    l=2
    
    childSums=[]
    
    if len(nums)<1:
        return 0,0
    
    children=nums[0]
    meta=nums[1]
    
    if children==0:
        return sum(nums[2:2+meta]), 2+meta
    
    else:
        for i in range(children):
            m,li=rec2(nums[l:])
            
            childSums.append(m)
            
            l+=li

        metas=nums[l:l+meta]
        
        for me in range(len(metas)):
            if metas[me]>children:
                f+=0
            else:
                f+=childSums[metas[me]-1]
        
        return f,l+meta
    
#answer part2
print(rec2(n)[0])