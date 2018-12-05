with open("in5.txt") as file:
    inS=file.read().rstrip()

done=False

def boom(c1,c2):
    if (c1.isupper() and c2.islower()) or (c1.islower() and c2.isupper()):
        if c1.lower()==c2.lower():
            return True
    return False

def exp(string,i):
    if len(string)<=2:
        return ''
    outStr=string.replace(string[i:i+2],'')    
    return outStr


def recurse(inStr):
    
    if len(inStr)<2:
        return inStr
    
    if len(inStr)==2:
        if boom(inStr[0],inStr[1]):
            return ''
        else:
            return inStr
    
    else:
        booms=0
        curLen=len(inStr)
        for i in range(len(inStr)):
            if i>=curLen-1:
                if booms==0:
                    print("returning")
                    return inStr
                else:
                    inStr=recurse(inStr)
            if boom(inStr[i],inStr[i+1]):
                booms+=1
                newStr=exp(inStr,i)
                inStr=recurse(newStr)  
                return inStr
                

outStr=recurse(inS)
 
#answer for part 1           
print(len(outStr))

bestl=len(inS)
for char in ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']:
    tryStr=inS.replace(char,'')
    tryStr=tryStr.replace(char.upper(),'')
    l=len(recurse(tryStr))
    if l<bestl:
        bestl=l
       
#answer for part 2
print(bestl)
    


