grades=[73,67,38,33]
chk=0
for i in range(len(grades)):
    if grades[i]<38:
        continue
    else:
        chk=grades[i]
        while True :
            if chk%5 == 0:
                if chk-grades[i]<3:
                    grades[i]=chk
                    break
                else:
                    break
            else:
                chk+=1

print(grades)
