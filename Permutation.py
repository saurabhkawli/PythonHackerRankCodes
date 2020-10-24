p=[4,3,5,1,2]
last=[]
for i in range(len(p)):
    i+=1
    for j in range(len(p)):
        if p[j] == i:
            k=j+1
            for j in range(len(p)):
                if p[j] == k:
                    last.append(j+1)
print(last)
