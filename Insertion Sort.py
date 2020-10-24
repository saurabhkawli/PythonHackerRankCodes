a=[1,4,3,5,6,2]
def printArray(a):
    x=""
    for number in a:
        x += str(number) + " "
    print (x)

for i in range(0, len(a)):
    j = i;
    while (j > 0 and a[j] < a[j-1]):
        temp = a[j];
        a[j] = a[j-1];
        a[j-1] = temp;
        j -= 1;
    if (i != 0): printArray(a)

def insertionSort2(n, arr):
    b=sorted(arr)
    i=0
    j=i+1
    while arr != b:
        if arr[i]<arr[j]:
            print(*arr, sep =' ')
        elif arr[i]>arr[j]:
            temp=arr[j]
            arr.remove(arr[j])
            for k in range(n):
                if arr[k]>temp:
                    arr.insert(k,temp)
                    print(*arr, sep =' ')
                    break
        i+=1
        j+=1

insertionSort2(6,(15,2,4,63,3,1))
