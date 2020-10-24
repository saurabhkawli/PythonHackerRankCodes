a=[1,2,3,4,5]
k=4

print("::::::::::::::::::::::::::::::::::::")
c=[]
sizea=len(a)-1
for i in range(k):
    b=[a[sizea]]+(a[0:sizea])
    a=b
print(b)
print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
a=[1,2,3,4,5]
c=[]
fact=k%len(a)
temp=a[len(a)-fact:]+a[:len(a)-fact]
print(temp)
