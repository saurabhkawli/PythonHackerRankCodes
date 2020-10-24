import math
n=4
start =5
countCum=0
for i in range(n):
   floorvalue=math.floor(start/2)
   print(floorvalue)
   start=floorvalue*3
   countCum+=floorvalue
print(countCum)
