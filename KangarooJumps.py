x1=43
v1=2
x2=70
v2=2

while x2>=x1 and v2<v1:
    print("X1 , X2",x1 ,x2)
    if x2 == x1:
        print("YES")
    elif x2 > x1:
        x1+=v1
        x2+=v2
print("NO")
