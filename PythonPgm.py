#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.

def compareTriplets(a, b):
    i=0
    alice=0
    bob=0
    while(i<3):
        if(a[i]>b[i]):
            alice+=1
        elif(a[i]<b[i]):
            bob+=1
        else:
            continue
        i+=1
    result = [alice,bob]
    print(result)
    return result
a = [1,3,4]
b = [3,2,7]

result = compareTriplets(a, b)

print(' '.join(map(str, result)))
print('\n')
