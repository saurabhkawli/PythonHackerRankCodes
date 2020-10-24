# Output Format
#
# Print the number of beautiful days in the inclusive range between  and .
#
# Sample Input
#
# 20 23 6
# Sample Output
#
# 2
i = 20
j = 23
k = 6

rev = []
for num in range(i, j + 1):
    revi = 0
    pre = num
    while num != 0:
        revi *= 10
        revi += num % 10
        num //= 10
    diff = abs(revi - pre) / k
    rev.append(diff)
count = 0
for ele in rev:
    if ele.is_integer():
        count += 1
print("Number of Good Days: ",count)
