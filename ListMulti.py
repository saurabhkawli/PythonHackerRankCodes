def re():
    a=[4,1,9,7]
    a=sorted(a)
    m=4
    i=1
    result=0
    while a != []:
        if len(a)/2 <= m:
            result +=i*sum(a[0:])
            return result
        result += i*sum(a[0:m])
        i+=1
        for j in range(m):
            a.remove(a[0])
    return result

print(re())
