import math
s="if man was meant to stay on the ground god would have given us roots"
s="feedthedog"
strips=s.replace(' ','')
lens=len(s.replace(' ',''))
sqrtofs = math.sqrt(lens)
floors=math.floor(sqrtofs)
ceils=math.ceil(sqrtofs)
count=0
newstr=''
for i in strips:
    count+=1
    newstr+=i
    if count==ceils:
        newstr+=' '
        count=0
print(newstr)
encrypt=''
newcount=0
cofloor=1
while len(encrypt)<len(newstr):
    for i in newstr:
        newcount+=1
        if newcount==cofloor:
            encrypt+=i
        elif newcount==ceils+1:newcount=0
    encrypt+=' '
    cofloor+=1
    newcount=0
    print(cofloor)
    if cofloor==ceils+1:
        break
print(encrypt)

