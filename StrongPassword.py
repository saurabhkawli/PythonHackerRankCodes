numbers = "0123456789"
lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
special_characters = "!@#$%^&*()-+"
count=0
main=0
password="g1A!"
for i in password:
    if i in numbers:
        count+=1
        break
for i in password:
    if i in lower_case:
        count+=1
        break
for i in password:
    if i in upper_case:
        count+=1
        break
for i in password:
    if i in special_characters:
        count+=1
        break
if count<4:
    main = 4-count
if len(password)<=6:
    lent = 6-len(password)
    if lent>main:
        print(lent)
    else:
        print(main)
print(main)
