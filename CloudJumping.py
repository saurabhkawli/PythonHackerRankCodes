c=[1,1,0,1,0,1,0,1,0,1,0,1,1,0,1,1,1,1,1]
k=19
i=0
i+=k
count=0
while i != 0:
    if i >= len(c):i=i-(len(c))
    if i==0:break
    if c[i]==1:count += 3
    else : count +=1
    i+=k

    if count > 20 : break
if c[i] == 0:print(count+1)
elif c[i] == 1:print(count+3)
